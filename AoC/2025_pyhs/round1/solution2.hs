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

initialState :: PhoneState
initialState = PhoneState 50 0

updatePhoneState :: PhoneState -> String -> PhoneState
updatePhoneState (PhoneState pos acc) ('R' : xs) = PhoneState newPos newAcc
  where
    newPos = mod (pos + read xs) 100
    newAcc = if newPos == 0 then acc + 1 else acc

updatePhoneState (PhoneState pos acc) ('L' : xs) = PhoneState newPos newAcc
  where
    newPos = mod (pos - read xs) 100
    newAcc = if newPos == 0 then acc + 1 else acc

updatePhoneState state _ = state -- for completeness (won't happen)

main :: IO ()
main = do
  content <- readFile "input.txt"
  let rotations = words content
      finalState = foldl' updatePhoneState initialState rotations
  print $ acc finalState

--1132