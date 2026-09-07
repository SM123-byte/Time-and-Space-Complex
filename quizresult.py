quiz_scores = [45, 62, 78, 85, 91, 56, 73, 88]

print("QUIZ RESULT SEARCHER")
print("Scores:", quiz_scores)
print("DIRECT ACCESS")
print("Score:", quiz_scores[0])
print("Complexity: O(1), Ω(1), Θ(1)")

#First have to linear search

target = 88
steps = 0

for score in quiz_scores:
    steps += 1
    if score == target:
        break

print("LINEAR SEARCH")
print("Target:", target)
print("Steps:", steps)
print("Best Case: Ω(1)")
print("Average Case: Θ(n)")
print("Worst Case: O(n)")

#Then, mark out in pairs
pair_steps = 0

for score1 in quiz_scores:
    for score2 in quiz_scores:
        pair_steps += 1

print("PAIR COMPARISON")
print("Pair Checks:", pair_steps)
print("Complexity: O(n²), Ω(n²), Θ(n²)")

# Case demonstration
print("SEARCH CASES")
for target in [45, 85, 88]:
    steps = 0
    for score in quiz_scores:
        steps += 1
        if score == target:
            break
    print(target, "->", steps, "steps")
