module Main where

import Data.List
import System.IO

-- Utility functions for character replacement
replace :: Char -> Char -> Char
replace target c
    | c == target = ' '
    | otherwise = c

replaceComma = replace ','
replaceDash = replace '-'

-- Input function to read and process the input file
readInput :: String -> IO [String]
readInput fname = do
  content <- readFile fname
  return $ words (map replaceComma content)

-- Logic ->

asRange :: String -> [Int]
asRange s = [start .. end]
    where x  =  map (\x -> read x :: Int) $ words (map replaceDash s)
          start = x !! 0
          end = x !! 1

feasibleSizes :: String -> [Int]
feasibleSizes s = filter (\x -> length s `mod` x == 0) [1 .. n]
    where n = length s `div` 2

repeats :: String -> Int -> Bool
-- repeats [] _ = True
repeats xs sz 
    | null rest = True
    | otherwise = isPrefixOf pattern rest && repeats rest sz
    where (pattern, rest) = splitAt sz xs

isInvalid :: Int -> Bool
isInvalid x = or checks
        where s = show x
              sizes = feasibleSizes s
              checks = map (repeats s) sizes


main :: IO ()
main = do
    input <- readInput "input.txt" -- list of ranges as strings
    -- printOutput input
    let invalids = [x | s <- input, x <- asRange s, isInvalid x]
    print $ sum invalids



