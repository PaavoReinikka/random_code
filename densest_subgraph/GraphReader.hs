module GraphReader where
import System.IO

readInput :: FilePath -> IO [String]
readInput path = do
    contents <- readFile path
    return (lines contents)

printLines :: [String] -> IO ()
printLines = mapM_ putStrLn

data Edge = Edge { fromNode :: Int, toNode :: Int } deriving (Show, Eq)
data Graph = Graph { edges :: [Edge], n_nodes :: Int } deriving (Show, Eq)

replaceWithSpace :: Char -> Char -> Char -> Char
replaceWithSpace target replacement char =
    if char == target then replacement else char

replaceCommas :: String -> String
replaceCommas = map (replaceWithSpace ',' ' ')

asEdge :: String -> Edge
asEdge line = let [fromStr, toStr] = words (replaceCommas line)
                  in Edge (read fromStr) (read toStr)

-- Example usage:
main :: IO ()
main = do
    lines <- readInput "dolphins.csv"
    let dataLines = drop 1 lines  -- Skip header
        graph = Graph (map asEdge dataLines) (length dataLines)
    print graph

