require("@nomicfoundation/hardhat-toolbox");

/** @type import('hardhat/config').HardhatUserConfig */
module.exports = {
  solidity: "0.8.18",
  networks: {
    anvil: {
        url: "http://192.168.3.164:8545",
        chainId: 31337,
        accounts: [PK],
    },
    goerli: {
        url: "https://goerli.infura.io/v3/92983deb8689407bb1736bdf82bf9c9c",
        chainId: 5,
        accounts: [PK],
    },
    mainnet: {
        url: "https://mainnet.infura.io/v3/92983deb8689407bb1736bdf82bf9c9c",
        chainId: 1,
        accounts: [PK],
    },
    lixbtest: {
        url: "https://test.lixb.io",
        chainId: 2888,
        accounts: [PK],
    },
    lixb: {
        url: "https://lixb.io",
        chainId: 1888,
        accounts: [PK],
    },
  },
};
