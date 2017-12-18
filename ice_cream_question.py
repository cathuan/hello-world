import numpy as np
from collections import namedtuple


Args = namedtuple("Args", ["truck_capacity", "freezer_capacity",
                           "truck_cost", "storage_cost"])

SubSchedule = namedtuple("SubSchedule", ["days", "volume_in_freezer"])


'''
The key idea is that the following min cost function can be calculated inductively:
min_cost(demanded_volumes, volume_in_freezer) = \
    min_{ordered_volume}[local_cost(ordered_volume) + carry_over_cost(carry_over_volume) + \
    min_cost(demanded_volumes[1:], carry_over_volume))]
where
- LHS:
    - demanded_volumes = [v1,v2,...,vn], a sequence of required volume of icecream for each days.
    - volume_in_freezer = the volume of icecream in the freezer at day 1
    - min_cost(demanded_volumes, volume_in_freezer) = minimum cost if we want to
        supply demanded_volumes icecreams in n days, given that at day 1 there are
        volume_in_freezer serves of icecreams in the freezer

- RHS:
    - ordered_volume = the number of icecreams we want to order on day 1
    - local_cost(ordered_volumer) = cost we need to order ordered_volume serves of icecream
    - carry_over_volume = after we order ordered_volume icecreams on day 1 and
        supply demanded_volumes[0] icecreams to the shop, the left icecreams,
        which will be stored in the freezer and carry over to the next day.
        It can be calculated as ordered_volume + volume_in_freezer - demanded_volumes[0]
    - carry_over_cost(carry_over_volume) = cost we need to store carry_over_volume icecreams
        in the freezer for one day.
    - min_cost(demanded_volumes[1:], carry_over_volume)) = minimum cost if we want to
        supply demanded_volumes[1:] icecreams from day 2 to day n, given that at day 2 there are
        carry_over_volume serves of icecreams in the freezer

Fix demanded_volumes. Without loss of generality, we assume 0 <= vi <= truck_capacity.
By induction:
- For any volume_in_freezer, we can calculate min_cost(demanded_volumes[-1:], volume_in_freezer)
- For any 0 < i <= len(demanded_volumes), suppose we know min_cost(demanded_volumes[i:], volume_in_freezer) for any
    0 <= volume_in_freezer <= freezer_capacity. Because
        - 0 <= ordered_volume <= truck_capacity i.e. we will never order more than one truck of icecream.
            If on day 1, we want to order 2 trucks of icecreams (ordered_volume > truck_capacity),
            and consume v1 < truck_capacity of icecreams. We will carry over $ordered_volume - v1$ icecreams to day 2.
            But we can always order one truck of icecream on day 1, and carry over $truck_capacity - v1$ icreams to day 1,
            and order extra $ordered_volume - truck_capacity$ icecreams on day 2, with the same truck cost,
            but less storage cost.
        - local_cost(ordered_volume) and carry_over_cost(carry_over_volume) can be calculated directly.
    we can calculate local_cost(ordered_volume) + carry_over_cost(carry_over_volume) + min_cost(demanded_volumes[i:], carry_over_volume)
    for all possible ordered_volume. So we can find the minimum of these values,
    which equals min_cost(demanded_volumes[i-1:], volume_in_freezer).

By the above two induction processes, we are able to calculate min_cost(demanded_volumes, volume_in_freezer).
Actually, min_cost(demanded_volumes, 0) is the number we want to calculate.
'''


# calcualte local_cost(ordered_volume)
def calculate_local_cost(ordered_volume, args):

    return args.truck_cost if ordered_volume != 0 else 0


# calculate carry_over_cost(carry_over_volume)
def calculate_carry_over_cost(carry_over_volume, args):
    return carry_over_volume * args.storage_cost


# For a given volume_in_freezer, and knowing all
# min_cost(demanded_volumes[i:], volume_in_freezer) with 1 <= i <= len(demanded_volumes)-1,
# calculate min_cost(demanded_volumes[i-1:], volume_in_freezer)
def calculate_cost_with_volume_in_freezer(demanded_volumes, volume_in_freezer, args, min_costs, min_cost_decisions):

    costs = []
    decisions = []

    for ordered_volume in range(args.truck_capacity+1):
        current_volume = ordered_volume + volume_in_freezer
        carry_over_volume = current_volume - demanded_volumes[0]

        # remove unrealistic carry over volume
        if carry_over_volume < 0 or carry_over_volume > args.freezer_capacity:
            continue

        local_cost = calculate_local_cost(ordered_volume, args)
        carry_over_cost = calculate_carry_over_cost(carry_over_volume, args)
        days = len(demanded_volumes)
        sub_schedule = SubSchedule(days-1, carry_over_volume)
        prev_step_min_cost = min_costs[sub_schedule]
        costs.append(local_cost + carry_over_cost + prev_step_min_cost)
        decisions.append([ordered_volume] + min_cost_decisions[sub_schedule])

    index = np.argmin(costs)
    return costs[index], decisions[index]


# - calculate min_cost(demanded_volumes[-1:], volume_in_freezer))
# - given min_cost(demanded_volumes[i:], volume_in_freezer)) (saved in min_costs)
#   for all carry_over, we can calculate min_cost(demanded_volumes[i-1:], volume_in_freezer)),
#   with all possible volume_in_freezer.
def calculate_min_costs_decisions(demanded_volumes, args, min_costs, min_cost_decisions):

    days = len(demanded_volumes)
    assert days > 0
    available_freezer_volumes = range(args.freezer_capacity+1)
    if days == 1:
        for volume_in_freezer in available_freezer_volumes:
            sub_schedule = SubSchedule(days, volume_in_freezer)
            if volume_in_freezer > demanded_volumes[0]:
                min_costs[sub_schedule] = np.inf
                min_cost_decisions[sub_schedule] = []
            elif volume_in_freezer < demanded_volumes[0]:
                min_costs[sub_schedule] = args.truck_cost
                min_cost_decisions[sub_schedule] = [demanded_volumes[0] - volume_in_freezer]
            else:
                min_costs[sub_schedule] = 0
                min_cost_decisions[sub_schedule] = [0]
    else:
        for volume_in_freezer in available_freezer_volumes:
            sub_schedule = SubSchedule(days, volume_in_freezer)
            cost, decision = calculate_cost_with_volume_in_freezer(demanded_volumes, volume_in_freezer, args, min_costs, min_cost_decisions)
            min_costs[sub_schedule] = cost
            min_cost_decisions[sub_schedule] = decision


# inductively calculate all min_cost(demanded_volumes[i:], volume_in_freezer)),
# for any 1 <= i <= len(demanded_volumes)-1, and all possible volume_in_freezer.
def initialize(demanded_volumes, args):

    min_costs = {}
    min_cost_decisions = {}

    for i in range(1,len(demanded_volumes)):
        calculate_min_costs_decisions(demanded_volumes[-i:], args, min_costs, min_cost_decisions)
    return min_costs, min_cost_decisions


if __name__ == "__main__":

    # set up the fixed variables for the scheduling
    truck_capacity = 3
    freezer_capacity = 10
    truck_cost = 10
    storage_cost = 1
    args = Args(truck_capacity, freezer_capacity, truck_cost, storage_cost)

    demanded_volumes = np.random.randint(0,10,5)
    #demanded_volumes = [2,0,2,2]

    residual_demanded_volumes = np.array(demanded_volumes) % truck_capacity
    fixed_demanded_volumes = np.array(demanded_volumes) / truck_capacity

    min_costs, min_cost_decisions = initialize(residual_demanded_volumes, args)
    cost, decision = calculate_cost_with_volume_in_freezer(residual_demanded_volumes, 0, args, min_costs, min_cost_decisions)

    cost += cost + fixed_demanded_volumes.sum() * truck_cost
    decision = np.array(decision) + fixed_demanded_volumes * truck_capacity

    print "demanded volumes is %s" % demanded_volumes
    print "minimum cost is %s" % cost
    print "volume required to order by day is %s" % decision
