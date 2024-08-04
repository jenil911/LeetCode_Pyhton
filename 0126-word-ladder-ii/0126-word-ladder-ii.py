class Solution:
    def findLadders(
        self, beginWord: str, endWord: str, wordList: List[str]
    ) -> List[List[str]]:
        def neighbors(word):
            for i in range(len(word)):
                for char in "abcdefghijklmnopqrstuvwxyz":
                    yield word[:i] + char + word[i + 1 :]

        i = 1
        words = {beginWord: lambda: [[beginWord]]}
        unvisited = set(wordList)
        while words and endWord not in words:
            i += 1
            new_words = defaultdict(lambda: lambda: [])
            for s in words:
                for ss in neighbors(s):
                    if ss in unvisited:

                        def get_seqs(capture=(ss, new_words[ss], words[s])):
                            ss, ss_get_seqs, s_get_seqs = capture
                            seqs = ss_get_seqs()
                            for seq in s_get_seqs():
                                seq.append(ss)
                                seqs.append(seq)
                            return seqs

                        new_words[ss] = get_seqs
            words = new_words
            unvisited -= words.keys()
        return words[endWord]()