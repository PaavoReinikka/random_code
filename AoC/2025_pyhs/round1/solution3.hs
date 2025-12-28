module Main where

import Data.List
import System.IO

--Alternative approach using a data structure to hold state
-- This makes the state updates easier to extend or modify in the future

data PhoneState = PhoneState
  { pos :: Int,
    acc :: Int
  }
  deriving (Show)

initState :: PhoneState
initState = PhoneState 50 0

--State update function
updatePhoneState :: PhoneState -> String -> PhoneState
--Right rotation case
updatePhoneState (PhoneState pos acc) ('R' : xs) = PhoneState newPos newAcc
  where
    steps = read xs
    newPos = mod (pos + steps) 100
    firstHit = 100 - pos
    newAcc = if steps < firstHit then acc else acc + 1 + quot (steps - firstHit) 100
--Left rotation case
updatePhoneState (PhoneState pos acc) ('L' : xs) = PhoneState newPos newAcc
  where
    steps = read xs
    newPos = mod (pos - steps) 100
    firstHit = if pos == 0 then 100 else pos
    newAcc = if steps < firstHit then acc else acc + 1 + quot (steps - firstHit) 100
--Fallback case (won't happen with valid input)
updatePhoneState state _ = state


main :: IO ()
main = do
  content <- readFile "input.txt"
  let rotations = words content
      finalState = foldl' updatePhoneState initState rotations
  print $ acc finalState

--6623