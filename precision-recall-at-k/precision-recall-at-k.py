def precision_recall_at_k(recommended, relevant, k):
    """
    Compute precision@k and recall@k for a recommendation list.
    """
    # Write code here
    recommended = recommended[:k]
    recommended = set(recommended)
    relevant = set(relevant)

    allRelevant = 0
    for num in recommended:
        if num in relevant:
            allRelevant += 1

    print(allRelevant)
    print(k)

    precision = allRelevant / k
    recall = allRelevant / len(relevant)


    return [precision, recall]