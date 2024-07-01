class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        ans = []
        n = len(s)
        if not (4 <= n <= 12):
            return ans

        def backtrack(ip, start, dots):
            octet_length = octet_value = 0
            for i in range(start, min(n, start+3)):
                ip.append(s[i])
                octet_length += 1
                octet_value = octet_value * 10 + int(s[i])
                if (octet_length > 1 and ip[-octet_length] == '0') or octet_value > 255:
                    return octet_length
                if i + 1 == n and not dots:
                    ans.append(''.join(ip))
                elif (n-1) - i <= (dots-1) * 3 + 3:
                    ip.append('.')
                    last_octet_length = backtrack(ip, i+1, dots-1)
                    for _ in range(last_octet_length + 1):
                        ip.pop()

            return octet_length

        backtrack([], 0, 3)
        return ans