{-# OPTIONS_GHC -fno-warn-tabs #-}
module Main where
--import qualified Data.HashSet as HashSet
import qualified Data.Set as HashSet
import Data.List

main :: IO ()
main = do
	str     <- getLine
	let ds  =  HashSet.singleton str
	let set =  foldr HashSet.insert ds $ permutations str
	print $ HashSet.size set
	mapM_ putStrLn $ sort $ HashSet.toList set
