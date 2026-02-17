# Problem solving challenge
# Given a jumbled collection of segments, each of which is represented as
# a Pair (startPoint, endPoint), this function sorts the segments to
# make a continuous path
# A few assumptions you can make:
# 1. Each particular segment goes in one direction only, i.e.: if you
# • see (1, 2), you will not see (2, 1).
# 2. Each starting point only have one way to the end point, i.e.: if
# -you see • (6, 5), you will not see• (6, 10), (6, 3), etc.
# For example, if you're passed a list containing the following intarrays:
# .. • [(4, 5), • (9, 4), • (5, •1), • (11, 9)]
# [(12,9), (9,4), (4,5), (5,1), (11,9)]
# Then your implementation should sort it such:
# • [ (11, 9), • (9, 4) , • (4, 5), (5, 1)] @param segments collection of segments, each represented by a Pair
# (startPoint, endPoint).
# @return • The sorted segments such that they form a continuous path.
# @throws Exception if there is no way to create one continuous path -from *all - the segments passed into this function. Feel -free to change the
# Exception type as you think appropriate.


def sort_segments(segments):
    # Map start -> end
    graph = dict(segments)

    # Find starts that aren't anyone's end
    ends = set(graph.values())
    heads = [s for s in graph if s not in ends]

    if len(heads) != 1:
        raise ValueError("Expected 1 starting point, found " + str(len(heads)))

    # Build path using recursion
    def build(start):
        if start not in graph:
            return []
        return [(start, graph[start])] + build(graph[start])

    result = build(heads[0])

    if len(result) != len(segments):
        raise ValueError("Cannot form one continuous path")

    return result


if __name__ == "__main__":
    # Test
    print(sort_segments([(4, 5), (9, 4), (5, 1), (11, 9)]))
    # [(11, 9), (9, 4), (4, 5), (5, 1)]

    # This will raise an error (multiple starting points)
    # print(sort_segments([(4, 5), (9, 4), (5, 1), (11, 9), (20, 30)]))