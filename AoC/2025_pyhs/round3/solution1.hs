module Main where

import Data.List
import Data.Char
import System.IO
import Distribution.Compat.CharParsing (digit)
import Distribution.Simple.Utils (xargs)


readInput :: String -> IO [String]
readInput fname = do
    content <- readFile fname
    return $ lines content

printInput :: [String] -> IO ()
printInput input = mapM_ putStrLn input

stringToInt :: String -> [Int]
stringToInt xs = [digitToInt x | x <- xs] -- has to be digits only

whereFirst :: [Int] -> Int -> Int -> Int -- Maybe Int
whereFirst (x:xs) target index = case x == target of True  -> index
                                                     False -> whereFirst xs target (index + 1)

whereMax :: [Int] -> Int
whereMax xs = whereFirst xs (maximum xs) 0

dropLast :: [a] -> [a]
dropLast xs = take (length xs - 1) xs

takeAfter :: Int -> [a] -> [a]
takeAfter ind xs = drop (ind + 1) xs -- guaranteed to be in bounds

getFstIndex :: String -> Int
getFstIndex s = whereMax $ stringToInt (dropLast s)

getJoltage :: String -> Int
getJoltage s = read joltage :: Int
    where ind = getFstIndex s
          digit1 = s !! ind : ""
          rest = [digitToInt c | c <- takeAfter ind s]
          digit2 = show $ maximum rest
          joltage = digit1 ++ digit2


main :: IO ()
main = do
    input <- readInput "input.txt"
    -- printInput input
    let total = sum $ map getJoltage input
    print total
