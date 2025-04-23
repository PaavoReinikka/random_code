
import benchmark
from algorithm import parallelize, vectorize
from Array import Matrix

def toMatrix(data: List[String], size: Int):
    var matrix = Matrix[1, size]()
    for i in range(size):
        matrix[0, i] = int(data[i])

@always_inline
fn truncate(val: String) raises -> String:
    return str(int(val))

#@parameter
fn blinkOne(val: String) raises -> String:
    if val == "0":
        return "1"
    elif len(val)%2==0:
        var k: Int = len(val)//2
        var left: String = truncate(val[0:k])
        var right: String = truncate(val[k:])
        return left + " " + right
    else:
        return str(int(val)*2024)

fn blink(mut stones: List[String]) raises -> None:# List[String]:
    var result: List[String] = List[String]()
    for stone in stones:
        var newstone: List[String] = blinkOne(stone[]).split(" ")
        result.append(newstone[0])
        if len(newstone) > 1:
            result.append(newstone[1])
    #return result
    stones = result

def printStones(stones: List[String]):
    for stone in stones:
        print(stone[], end=" ")
    print()

fn run() raises -> None:

    var stones: List[String] = "890 0 1 935698 68001 3441397 7221 27".split(" ")

    for i in range(25):
        blink(stones)
    
    var message: String = "Number of stones: " + str(len(stones))
    print(message)

def main():
    #var secs = benchmark.run[run]().mean()
    #print("Average time: " + str(secs))
    run()