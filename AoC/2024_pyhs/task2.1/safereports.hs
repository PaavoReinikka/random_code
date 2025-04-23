
module SafeReports where
    
import Data.List

toIntegerList :: [String] -> [Integer]
toIntegerList = map (\str -> read str :: Integer)

increasingValid :: [Integer] -> Bool
increasingValid [x] = True
increasingValid (x:y:xs) = diff <=3 && 1<=diff && increasingValid (y:xs)
                          where diff = y-x

decreasingValid :: [Integer] -> Bool
decreasingValid [x] = True
decreasingValid (x:y:xs) = diff <=3 && 1<=diff && decreasingValid (y:xs)
                          where diff = x-y

valid1 :: [Integer] -> Bool
valid1 xs = increasingValid xs || decreasingValid xs

validBool :: [Integer] -> Bool
validBool xs = increasingValid xs || decreasingValid xs

-- indexing from 0
dropAt :: Int -> [Integer] -> [Integer]
dropAt n xs = take n xs ++ drop (n+1) xs

valid2 :: [Integer] -> Bool
valid2 xs = any validBool (map (\n -> dropAt n xs) [0..length xs - 1])

valid :: [Integer] -> Int
valid xs = fromEnum (valid1 xs || valid2 xs)

main :: IO ()
main = do
    text <- readFile("input.txt")
    let textlines = lines text
    let textlists = map words textlines

    let values = map toIntegerList textlists
    
    let validReports = map valid values
    let count =  sum validReports
    print count


