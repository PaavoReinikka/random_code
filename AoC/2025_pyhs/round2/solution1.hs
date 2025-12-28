module Main where

import Data.List
import System.IO
import Data.Time.Format.ISO8601 (recurringIntervalFormat)

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

-- Output function for testing
printOutput :: [String] -> IO ()
printOutput [] = return ()
printOutput (x:xs) = do
  putStrLn x
  printOutput xs

-- Logic to determine if a number is invalid
isInvalid :: Int -> Bool
isInvalid x
    | odd (length s) = False
    | otherwise = t == h
        where h = take (length s `div` 2) s
              t = drop (length s `div` 2) s
              s = show x

-- Convert a range string to a list of integers
asRange :: String -> [Int]
asRange s = [start .. end]
    where x  =  map (\x -> read x :: Int) $ words (map replaceDash s)
          start = x !! 0
          end = x !! 1


main :: IO ()
main = do
    input <- readInput "input.txt" -- list of ranges as strings
    let invalids = [x | s <- input, x <- asRange s, isInvalid x]
    print $ sum invalids



