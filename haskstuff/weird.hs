{-# OPTIONS_GHC -fno-warn-tabs #-}
module Main where

	weird :: Int -> IO ()
	weird 1 = putStr "1\n"
	weird n | even n    = do
					let newn = n `div` 2 :: Int 
					putStr $ show n ++ " "
					weird newn
			| otherwise = do
					let newn = 3*n + 1
					putStr $ show n ++ " "
					weird newn


	modifyArr :: [Int] -> Int -> Int
	modifyArr [] acc                     = acc
	modifyArr [x] acc                    = acc
	modifyArr (x:y:rest) acc | x>y       = modifyArr (x:rest) (acc + x - y) 
							 | otherwise = modifyArr (y:rest) acc

	main :: IO ()
	main = do
		n <- getLine
		arrStr <- getLine
		let arr = map (\x -> read x :: Int) $ words arrStr
		let result = modifyArr arr 0
		print $ result
		--weird n'
