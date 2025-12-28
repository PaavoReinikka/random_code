module Main where

import Data.List
import System.IO


readInput :: String -> IO [String]
readInput fname = do
    content <- readFile fname
    return $ lines content

printInput :: [String] -> IO ()
printInput input = mapM_ putStrLn input

main :: IO ()
main = do
    input <- readInput "input.txt"
    printInput input
