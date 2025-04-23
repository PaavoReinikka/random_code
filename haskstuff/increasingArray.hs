{-# OPTIONS_GHC -fno-warn-tabs #-}
module Main where

	modifyArr :: [Int] -> Int -> Int
	modifyArr [_] acc                    = acc
	modifyArr (x:y:rest) acc | x>y       = modifyArr (x:rest) (acc + x - y) 
							 | otherwise = modifyArr (y:rest) acc

	main :: IO ()
	main = do
		_       <- getLine
		arrStr  <- getLine
		let arr = map (\x -> read x :: Int) $ words arrStr
		print $ modifyArr arr 0

