module Similarity where
import Prelude


getEvens :: [Integer] -> [Integer]
getEvens [] = []
getEvens (x:y:xs) = x : getEvens xs

getOdds :: [Integer] -> [Integer]
getOdds [] = []
getOdds (x:y:xs) = y : getOdds xs

count :: Integer -> [Integer] -> Integer
count n [] = 0
count n (x:xs) = if x == n then 1 + count n xs else count n xs

main :: IO ()
main = do
    text <- readFile("input.txt")
    let values = map (\str -> read str :: Integer) (words text)

    let left = getEvens values
    let right = getOdds values

    let counts = [count n right | n <- left]
    let similarity = zipWith (\x y -> x * y) left counts

    print (sum similarity)
    

