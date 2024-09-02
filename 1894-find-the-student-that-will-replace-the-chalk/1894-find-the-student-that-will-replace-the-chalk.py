class Solution:
    def chalkReplacer(self, chalk: List[int], initialChalkPieces: int) -> int:
        totalChalkNeeded = sum(chalk)
        remainingChalk = initialChalkPieces % totalChalkNeeded
        
        for studentIndex, studentChalkUse in enumerate(chalk):
            if remainingChalk < studentChalkUse:
                return studentIndex
            remainingChalk -= studentChalkUse
        
        return 0




def kdsmain():
    input_data = sys.stdin.read().strip()
    lines = input_data.splitlines()
    
    num_test_cases = len(lines) // 2
    results = []

    for i in range(num_test_cases):
        chalk = json.loads(lines[i*2])
        initialChalkPieces = int(lines[i*2 + 1])
        
        result = Solution().chalkReplacer(chalk, initialChalkPieces)
        results.append(str(result))

    with open('user.out', 'w') as f:
        for result in results:
            f.write(f"{result}\n")

if __name__ == "__main__":
    kdsmain()
    exit(0)
