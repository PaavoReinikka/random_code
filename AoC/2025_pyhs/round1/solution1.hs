module Main where

import Data.List
import System.IO

readInput :: String -> IO [Int]
readInput fname = do
  content <- readFile fname
  return $ map stringToInt (words content)

stringToInt :: String -> Int
stringToInt ('R' : xs) = read xs :: Int
stringToInt ('L' : xs) = (-1) * (read xs :: Int)
stringToInt xs = read xs :: Int -- for completeness (won't happen)

rotate :: Int -> Int -> Int
rotate dx x = mod (x + dx) 100

accumulator :: [Int] -> Int -> Int -> Int
accumulator [] _ acc = acc
accumulator (dx : xs) x acc = case rotate dx x of
  0 -> accumulator xs 0 (acc + 1)
  new_x -> accumulator xs new_x acc

main = do
  rotations <- readInput "input.txt"
  let final_pos = accumulator rotations 50 0
  print final_pos
