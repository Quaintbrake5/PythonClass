# 4. Rank Students by Average Score
def rank_students(scores):
    result = [(name, round(sum(marks)/len(marks), 2))
              for name, marks in scores.items()
            ]
    return sorted(result, key=lambda x: (-x[1], x[0]))

# Example
print(rank_students({'Alice':[90,85,88], 'Bob':[90,85,88], 'Charlie':[95,80,85]}))