module Main where

import Data.List
import System.IO
import Data.ByteString (count)

--Alternative approach using a data structure to hold state
-- This makes the state updates easier to extend or modify in the future

data PhoneState = PhoneState
  { pos :: Int,
    acc :: Int
  }
  deriving (Show)

countHitsZeroR :: Int -> Int -> Int -> Int
countHitsZeroR pos steps acc
  | steps <= 0 = acc
  | otherwise = countHitsZeroR (pos+1 `mod` 100) (steps -1) (if (pos +1) `mod` 100 == 0 then acc +1 else acc)

countHitsZeroL :: Int -> Int -> Int -> Int
countHitsZeroL pos steps acc
  | steps <= 0 = acc
  | otherwise = countHitsZeroL (pos-1 `mod` 100) (steps -1) (if (pos -1) `mod` 100 == 0 then acc +1 else acc)

updatePhoneState :: String -> PhoneState -> PhoneState
updatePhoneState ('R' : xs) (PhoneState pos acc) = PhoneState newPos newAcc
  where
    steps = read xs
    newPos = (pos + steps) `mod` 100
    newAcc = countHitsZeroR pos steps acc
updatePhoneState ('L' : xs) (PhoneState pos acc) = PhoneState newPos newAcc
  where
    steps = read xs
    newPos = (pos - steps) `mod` 100
    newAcc = countHitsZeroL pos steps acc
updatePhoneState _ state = state -- for completeness (won't happen)

processRotations :: [String] -> PhoneState -> PhoneState
processRotations [] state = state
processRotations (!r : rs) state = processRotations rs (updatePhoneState r state)

main :: IO ()
main = do
  content <- readFile "input.txt"
  let rotations = words content
      initialState = PhoneState 50 0
      finalState = processRotations rotations initialState
  print $ acc finalState

--6623