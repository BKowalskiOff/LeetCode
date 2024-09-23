class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        out = ["" for _ in range(n)]
        for i in range(1, n+1):
            if i%15 == 0:
                out[i-1] = "FizzBuzz"
                continue
            if i%3 == 0:
                out[i-1] = "Fizz"
                continue
            if i%5 == 0:
                out[i-1] = "Buzz"
                continue
            out[i-1] = str(i)
        return out