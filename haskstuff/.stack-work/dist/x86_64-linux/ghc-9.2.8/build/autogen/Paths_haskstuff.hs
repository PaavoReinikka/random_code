{-# LANGUAGE CPP #-}
{-# LANGUAGE NoRebindableSyntax #-}
{-# OPTIONS_GHC -fno-warn-missing-import-lists #-}
{-# OPTIONS_GHC -w #-}
module Paths_haskstuff (
    version,
    getBinDir, getLibDir, getDynLibDir, getDataDir, getLibexecDir,
    getDataFileName, getSysconfDir
  ) where


import qualified Control.Exception as Exception
import qualified Data.List as List
import Data.Version (Version(..))
import System.Environment (getEnv)
import Prelude


#if defined(VERSION_base)

#if MIN_VERSION_base(4,0,0)
catchIO :: IO a -> (Exception.IOException -> IO a) -> IO a
#else
catchIO :: IO a -> (Exception.Exception -> IO a) -> IO a
#endif

#else
catchIO :: IO a -> (Exception.IOException -> IO a) -> IO a
#endif
catchIO = Exception.catch

version :: Version
version = Version [0,0,1] []

getDataFileName :: FilePath -> IO FilePath
getDataFileName name = do
  dir <- getDataDir
  return (dir `joinFileName` name)

getBinDir, getLibDir, getDynLibDir, getDataDir, getLibexecDir, getSysconfDir :: IO FilePath



bindir, libdir, dynlibdir, datadir, libexecdir, sysconfdir :: FilePath
bindir     = "/home/paavo/projects/haskstuff/.stack-work/install/x86_64-linux/55bbc3949eed31e555e29866ed0443716147e3ddf9eeb8125ee58e08eb6eebfa/9.2.8/bin"
libdir     = "/home/paavo/projects/haskstuff/.stack-work/install/x86_64-linux/55bbc3949eed31e555e29866ed0443716147e3ddf9eeb8125ee58e08eb6eebfa/9.2.8/lib/x86_64-linux-ghc-9.2.8/haskstuff-0.0.1-4KrCGm9HYhLJJ0O2519xHQ"
dynlibdir  = "/home/paavo/projects/haskstuff/.stack-work/install/x86_64-linux/55bbc3949eed31e555e29866ed0443716147e3ddf9eeb8125ee58e08eb6eebfa/9.2.8/lib/x86_64-linux-ghc-9.2.8"
datadir    = "/home/paavo/projects/haskstuff/.stack-work/install/x86_64-linux/55bbc3949eed31e555e29866ed0443716147e3ddf9eeb8125ee58e08eb6eebfa/9.2.8/share/x86_64-linux-ghc-9.2.8/haskstuff-0.0.1"
libexecdir = "/home/paavo/projects/haskstuff/.stack-work/install/x86_64-linux/55bbc3949eed31e555e29866ed0443716147e3ddf9eeb8125ee58e08eb6eebfa/9.2.8/libexec/x86_64-linux-ghc-9.2.8/haskstuff-0.0.1"
sysconfdir = "/home/paavo/projects/haskstuff/.stack-work/install/x86_64-linux/55bbc3949eed31e555e29866ed0443716147e3ddf9eeb8125ee58e08eb6eebfa/9.2.8/etc"

getBinDir     = catchIO (getEnv "haskstuff_bindir")     (\_ -> return bindir)
getLibDir     = catchIO (getEnv "haskstuff_libdir")     (\_ -> return libdir)
getDynLibDir  = catchIO (getEnv "haskstuff_dynlibdir")  (\_ -> return dynlibdir)
getDataDir    = catchIO (getEnv "haskstuff_datadir")    (\_ -> return datadir)
getLibexecDir = catchIO (getEnv "haskstuff_libexecdir") (\_ -> return libexecdir)
getSysconfDir = catchIO (getEnv "haskstuff_sysconfdir") (\_ -> return sysconfdir)




joinFileName :: String -> String -> FilePath
joinFileName ""  fname = fname
joinFileName "." fname = fname
joinFileName dir ""    = dir
joinFileName dir fname
  | isPathSeparator (List.last dir) = dir ++ fname
  | otherwise                       = dir ++ pathSeparator : fname

pathSeparator :: Char
pathSeparator = '/'

isPathSeparator :: Char -> Bool
isPathSeparator c = c == '/'
