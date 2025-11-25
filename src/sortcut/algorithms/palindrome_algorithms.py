# palindrome_algorithms.py

def longest_palindrome(s: str) -> int:
    s_prime: str = '#' + '#'.join(s) + '#'
    n: int = len(s_prime)
    palindrome_radii: list[int] = [0] * n
    center = right = 0

    for i in range(n):
        mirror: int = 2 * center - i

        if i < right:
            palindrome_radii[i] = min(right - i, palindrome_radii[mirror])

        while (
            i + palindrome_radii[i] + 1 < n
            and i - palindrome_radii[i] - 1 >= 0
            and s_prime[i + palindrome_radii[i] + 1] == s_prime[i - palindrome_radii[i] - 1]
        ):
            palindrome_radii[i] += 1

        if i + palindrome_radii[i] > right:
            center = i
            right = i + palindrome_radii[i]

    max_length: int = max(palindrome_radii)
    return max_length


def longest_palindrome_str(s: str) -> str:
    if not s:
        return ""
    s_prime = '#' + '#'.join(s) + '#'
    n = len(s_prime)
    radii = [0] * n
    center = right = 0

    for i in range(n):
        mirror = 2 * center - i
        if i < right:
            radii[i] = min(right - i, radii[mirror])
        while (
            i + radii[i] + 1 < n
            and i - radii[i] - 1 >= 0
            and s_prime[i + radii[i] + 1] == s_prime[i - radii[i] - 1]
        ):
            radii[i] += 1
        if i + radii[i] > right:
            center = i
            right = i + radii[i]

    max_radius = max(radii)
    center_index = radii.index(max_radius)
    start = (center_index - max_radius) // 2
    end = start + max_radius
    return s[start:end]


def num_of_palindromes(s: str) -> int:
    count: int = 0
    for i in range(len(s)):
        # odd-length
        l = r = i
        while l >= 0 and r < len(s) and s[l] == s[r]:
            count += 1
            l -= 1
            r += 1
        # even-length
        l, r = i, i + 1
        while l >= 0 and r < len(s) and s[l] == s[r]:
            count += 1
            l -= 1
            r += 1
    return count


def palindromes_list(s: str) -> list[str]:
    pals: list[str] = []
    for i in range(len(s)):
        # odd-length
        l = r = i
        while l >= 0 and r < len(s) and s[l] == s[r]:
            pals.append(s[l:r+1])
            l -= 1
            r += 1
        # even-length
        l, r = i, i + 1
        while l >= 0 and r < len(s) and s[l] == s[r]:
            pals.append(s[l:r+1])
            l -= 1
            r += 1
    return pals
