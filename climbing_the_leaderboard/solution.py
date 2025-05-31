def climbingLeaderboard(ranked, player):
    unique_rank = get_unique_rank(ranked)
    num_ranks = len(unique_rank)
    starting_right_ptr = num_ranks - 1
    new_rank = []
    for p in player:
        rank = find_idx(unique_rank, p, starting_right_ptr) + 1
        starting_right_ptr = min(rank - 1, num_ranks - 1)
        new_rank.append(rank)
    return new_rank
    
    
def get_unique_rank(ranked):
    unique_rank = [ranked[0]]
    prev_rank = ranked[0]
    for rank in ranked[1:]:
        if rank == prev_rank:
            continue
        prev_rank = rank
        unique_rank.append(rank)
    return unique_rank

def find_idx(desc_sorted_arr, target, starting_right_ptr):
    left_ptr = 0
    right_ptr = starting_right_ptr
    while True:
        if right_ptr - left_ptr <= 1:
            if target >= desc_sorted_arr[left_ptr]:
                return left_ptr
            elif target < desc_sorted_arr[right_ptr]:
                return right_ptr + 1
            else:
                return right_ptr
        mid_ptr = (left_ptr + right_ptr) // 2
        if target == desc_sorted_arr[mid_ptr]:
            return mid_ptr
        elif target < desc_sorted_arr[mid_ptr]:
            left_ptr = mid_ptr
        else:
            right_ptr = mid_ptr

ranked = [65, 60]
player = [65, 65]
print(climbingLeaderboard(ranked, player))