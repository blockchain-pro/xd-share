# Hourse

## Overview

The Hourse is include a Hourse NFT and a Lootbox.

## Quick Start

```
yarn build
```

after the command finished, see the [doc](docs/index.html)

### Compile

```
yarn build
```

### Test

```
yarn test
```

### Test coverage

``` 
yarn coverage
```

### Static analysis

```
yarn slither
```

> before the execution, you should to [install](https://github.com/crytic/slither#how-to-install) for this command.

### Deploy

```
yarn deploy <anvil | goerli | mainet | lixbtest | lixb>
```

Use the `deploy` command to complete contract deployment, you need to setting the [lootbox] in [hardhat.config.js](./hardhat.config.js) for your environment and configure [.env](.env) for storing wallet private keys.

[.env](.env) like this:

```
PK=<private key>
```

and then [grant authorities](#grant-authorities)

### Grant Authorities

```shell
yarn  grant --name <HorseToken|HorseLootBox> --account <address of account> --role <APP|ADMIN> --network <anvil | goerli | mainet | lixbtest | lixb>
``` 

### Latest

You need use this command to call the `setApprovalForAll` function on `HorseToken` after the all of Horse NFTs has been minted and that will be enable the LootBox. You should be change the `PK` in [.env](.env) file to private key of account who has been HorseToken NFT's owner. 

```shell
yarn hardhat approvalall --operator <HorseLootBox address> --type HorseToken --network <anvil | goerli | mainet | lixbtest | lixb>
```