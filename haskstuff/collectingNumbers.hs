{-# OPTIONS_GHC -fno-warn-tabs #-}
module Main where
--import qualified Data.Map as Map
--import qualified Data.Map.Lazy as Map
import qualified Data.IntMap.Strict as Map
--import Todo
{--
helper' :: Map.Map Int Int -> Int -> Int -> Int
helper' m n acc = case Map.lookup n m of
	Nothing -> acc
	Just x  -> case Map.lookup (n+1) m of
		Nothing -> acc
		Just y  -> if x > y then 1+acc else acc
--}

main :: IO ()
main = do
	nstr <- getLine
	let n = read nstr :: Int
	vals <- getLine
	let arr = map (\x -> read x :: Int) $ words vals
	let m = Map.fromList $ zip arr [1..n]
	let helper n acc = case Map.lookup n m of
											Nothing -> acc
											Just x  -> case Map.lookup (n+1) m of
												Nothing -> acc
												Just y  -> if x > y then 1 + acc else acc
	{--	
	let helper n acc = do
		let next = Map.findWithDefault 0 (n+1) m
		if next == 0 then acc else do
			let this = Map.findWithDefault n n m
			if next < this then 1+acc else acc
	--}
	let rounds = foldr helper 1 [1..n]
	print rounds


