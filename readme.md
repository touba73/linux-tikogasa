# Linux-Tikogasa
My amd-zen2 improved kernel.

~~1.zfs support~~

2.ZSTD RAM and SWAP support

3.PDS CPU Scheduler

4.BMQ I/O Scheduler

5.Xanmod patch

6.Chinese TTY support

7.WineSync

8.Clearlinux patch

9.Build with llvm/clang/lld latest stable build and use LTO_thin

9.GRAYSKY2 patch for AMD ZEN2 CPU

## 更新版本

需要更改 `.github/workflows/main.yml` 中的 `title` `automatic_release_tag` ，改为`v+版本号`即可。  
以及 `PKGBUILD` 中的 `gitver`，直接修改为数字版本号。  
所有更改扔进一个 commit 里，因为 action 每检测到一个 commit 就会开始编译然后发布一个版本。  
