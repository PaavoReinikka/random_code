
module TotalDistance where

import Data.List
import Prelude
import System.IO
import Distribution.ModuleName (main)

-- function that readds an input file and returns a list of strings
readInput :: String -> IO [Int]
readInput filename = do
  contents <- readFile filename
-- each line of the file is a string of the form "someint someotherint"
-- parse the string into a list of integers, by "words" and "map read"
  return (stringToInt (words contents))

-- function that takes a list of strings and returns a list of integers
stringToInt :: [String] -> [Int]
stringToInt = map read

-- function that takes every even index of a list
everyEven :: [a] -> [a]
everyEven [] = []
everyEven (x:exclude:xs) = x : everyEven xs

-- function that takes every odd index of a list
everyOdd :: [a] -> [a]
everyOdd [] = []
everyOdd (exclude:x:xs) = x : everyOdd xs

-- function that  prints a list of integers
printList :: [Int] -> IO ()
printList [] = return ()
printList (x:xs) = do
  putStrLn (show x)
  printList xs

