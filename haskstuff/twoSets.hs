{-# OPTIONS_GHC -fno-warn-tabs #-}
module Main where
    
    helper :: Int -> Int -> [Int]
    helper acc n | acc < 0 = filter (/= (-acc)) [1..(n-1)]
                 | acc == 0 = [1..(n-1)]
                 | otherwise = helper (acc - n) (n + 1)

    helper2 :: Int -> Int -> Int -> ([Int], [Int])
    helper2 acc n m | acc < 0 = (xs, ys)
                    | acc == 0 = ([1..(n-1)], [n..m])
                    | otherwise = helper2 (acc - n) (n + 1) m
                    where xs = filter (/= (-acc)) [1..(n-1)]
                          ys = (-acc):[n..m]
    
    printArrPair :: ([Int], [Int]) -> IO ()
    printArrPair (xs, ys) = do
        putStrLn $ show $ length xs
        putStrLn $ unwords $ map show xs
        putStrLn $ show $ length ys
        putStrLn $ unwords $ map show ys

    maybeHalf :: String -> Maybe Int
    maybeHalf n = if even s then Just (s `div` 2) else Nothing
                  where s = k*(k+1) `div` 2
                        k = read n :: Int 
    



    main :: IO ()
    main = do
        n  <- getLine
        case maybeHalf n of
            Nothing -> putStrLn "NO"
            Just k  -> do
                putStrLn "YES"
                printArrPair $ helper2 k 1 (read n :: Int)
                --printArrPair (read n :: Int) $ helper k 1
