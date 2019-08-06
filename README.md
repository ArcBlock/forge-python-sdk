[![Gitter](https://badges.gitter.im/ArcBlock/community.svg)](https://gitter.im/ArcBlock/community?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge)

![forge-python-sdk](https://www.arcblock.io/.netlify/functions/badge/?text=Forge%20Python%20SDK)

For details about how to set up Forge, please checkout [Forge](https://github.com/ArcBlock/forge).

A more detailed reference manual for forge-python-sdk can be found [Here](https://docs.arcblock.io/forge-sdk/python/latest/).


## Installation

We recommend installing through `pip`
```sh
pip install forge-python-sdk
```
::: warning
This sdk supports python verison `>=3.6`.
:::

## Usage

### Step 0

First get your Forge running on local with [Forge CLI](https://docs.arcblock.io/forge/latest/tools/forge_cli.html).

### Step 1
Create a Forge Connection with your Forge port (Default is `127.0.0.1:28210` if your Forge runs with `forge-cli`)
```python
from forge_sdk import ForgeConn
f = ForgeConn('127.0.0.1:28210')
rpc = f.rpc
config = f.config
```
::: warning
This step applies to every tutorial
:::

## Tutorials

### Level 1: Transfer Money

**Scenario**: Alice wants to transfer 10 TBA to Mike.

::: tip Notes
**TBA** is the default currency on Forge Chain. If 1 TBA has 16 digits, it shows as `10000000000000000`.
:::

#### Step 1: create wallets for Alice and Mike

```python
from forge_sdk import protos, utils
alice = rpc.create_wallet(moniker='alice', passphrase='abc123')
mike = rpc.create_wallet(moniker='mike', passphrase='abc123')
```

::: tip Notes
`moniker` is a nickname for this wallet on Forge. `passphrase` is used by Forge to encrypt the wallet into a keystore file. More details about wallet declaration rules are [here](../intro/concepts).
:::

Let's take a look at Alice's wallet and here account details

```python
>>> alice
token: "886fe22cd8d29a5c0d0fa5b21ec448bd"
wallet {
  sk: "\274\262\331z\000\265\374\271O7f\2640<\214\212G\302y\021\232\363\355.E\207\213&\355\362\260Gu\204\360@e\036\353\357\276\323\340\211\371U\3716\2212\304\223\037{\037\366\267\374\233@\021\215W\027"
  pk: "u\204\360@e\036\353\357\276\323\340\211\371U\3716\2212\304\223\037{\037\366\267\374\233@\021\215W\027"
  address: "z1brhJCteRSvHUQ9BytsZePkY4KJ9LFBayC"
}

>>> rpc.get_account_balance(alice.wallet.address)
0
```

#### Step 2: Help Alice send a Poke Transaction to get some money

Now you have created wallets for Alice and Mike, but there's no money in their accounts. Let's help Alice to earn some money by sending a **Poke** transaction.

```python
>>> rpc.poke(alice.wallet)
hash: "CF0513E473ED13712CDB65EFC196A77BD6193E7DF5124C6233C55732573C85A2"
```
Receiving the **hash** means the transaction has been passed to Forge, but doens't mean the transaction is successful. To confirm that the transaction is sent successfully, let's dive deeper into the tranaction details.

```python
>>> rpc.is_tx_ok('CF0513E473ED13712CDB65EFC196A77BD6193E7DF5124C6233C55732573C85A2')
True
```

If `is_tx_ok` returns `True`, that means the transaction has been executed successfully. Now Alice should have 25 TBA in her account.

Now let's check Alice's account balance. There should be 25 TBA.

```python
>>> rpc.get_account_balance(alice.wallet.address)
250000000000000000
```

::: tip Notes
**Poke**: Each account can send a **Poke Transaction** to get 25 TBA each day.
**Hash**: The calculated hash of the signed transaction. Each transaction should have its own unique **hash**.
:::

#### Step 3: Transfer the money from Alice to Mike

Now Alice has 25 TBA in her account and Mike has nothing. We can help Alice transfer 10 TBA to Mike by sending out a **transfer transaction**.

```python
rpc.transfer(to=mike.wallet.address,value=utils.to_unit(100),wallet=alice.wallet)
 hash: "CAEF155B1A3A684DAF57C595F68821502BC0187BEC514E4660BA1BD568474345"

rpc.is_tx_ok('CAEF155B1A3A684DAF57C595F68821502BC0187BEC514E4660BA1BD568474345')
True

rpc.get_account_balance(mike.wallet.address)
101000000000000000
```

Now we can see tht Alice just successfully transferred 10 TBA to Mike's Account!

 🎉 Congratulations! You have finished the Level 1 tutorial! Now you should have a general sense about how Forge works. If you want more challenges, go checkout the Level 2 tutorial.

 ### Level 2: Sell a Used Laptop

 **Scenario**: Mike wants to sell a used laptop to Alice.

#### Step 1: Create accounts for Alice and Mike

```python
alice=rpc.create_wallet(moniker='alice', passphrase='abc123')
mike = rpc.create_wallet(moniker='mike', passphrase='abc123')
```

After creating accounts for Alice and Mike, we help Alice to get some money to buy Mike's laptop

```python

rpc.poke(alice.wallet, alice.token)
hash: "CF0513E473ED13712CDB65EFC196A77BD6193E7DF5124C6233C55732573C85A2"

rpc.get_account_balance(alice.wallet.address)
250000000000000000
```

#### Step 2: Create a laptop asset for Mike

In real world, Mike could have just sold Alice his laptop. With Forge SDK, any physical item can exist in the form of **asset**.

Let's try to help Mike create a laptop asset with the **CreateAssetTx**. The `data` field is for users to put item-specific information, where `type_url` is hints for how to decode the serialized `value` field. In this tutorial, for simplicity purpose, we only put the name of thel laptop.

```python
res, asset_address= rpc.create_asset('test:name:laptop', b'Laptop from Mike',mike.wallet, mike.token)
rpc.is_tx_ok(res.hash)
True
asset_address
'zjdwghZpZN45ig6ytP74r8VF9CHhQtEjBype'
```

Then we can see how the asset acutally look like.

```python
rpc.get_single_asset_state(asset_address)
address: "zjdwghZpZN45ig6ytP74r8VF9CHhQtEjBype"
owner: "z1QyzoxdPPEk9A2Uz6h18rvjsAHtmJ78mGD"
transferrable: true
issuer: "z1QyzoxdPPEk9A2Uz6h18rvjsAHtmJ78mGD"
stake {
  total_stakes {
    value: "\000"
  }
  total_unstakes {
    value: "\000"
  }
  total_received_stakes {
    value: "\000"
  }
  recent_stakes {
    type_url: "fg:x:address"
    max_items: 128
    circular: true
  }
  recent_received_stakes {
    type_url: "fg:x:address"
    max_items: 128
    circular: true
  }
}
context {
  genesis_tx: "9EAC9AF9136D30E5C02EDD46BEF081AD61F3F722BA6FEF4398CC5FBC363DCA30"
  renaissance_tx: "9EAC9AF9136D30E5C02EDD46BEF081AD61F3F722BA6FEF4398CC5FBC363DCA30"
  genesis_time {
    seconds: 1557129670
    nanos: 700917000
  }
  renaissance_time {
    seconds: 1557129670
    nanos: 700917000
  }
}
data {
  type_url: "test:name:laptop"
  value: "Laptop from Mike"
}
```

The laset field is the `data` field, where we can see `Laptop from Mike`. You can also put more complicated information inside, like serialized protobuf message.

#### Step 3 : Exchange the asset with money

Now Alice has 25 TBA in her account, and Mike has a laptop asset. What should Mike do if he wants to sell the laptop asset for 10 TBA? He can initiate an **ExchangeTx**.

Since Mike is going to be the sender, we put the laptop `asset_address` as what he will exchange. Similarly, Alice will exchange 10 TBA.

```python
mike_exchange_info = protos.ExchangeInfo(assets=[asset_address])
alice_exchange_info = protos.ExchangeInfo(value = utils.int_to_biguint(100000000000000000))
exchange_tx = protos.ExchangeTx(sender = mike_exchange_info, receiver=alice_exchange_info)

tx = rpc.prepare_exchange(exchange_tx, mike.wallet)
tx = rpc.finalize_exchange(tx, alice.wallet)
res = rpc.send_tx(tx)

>>> rpc.is_tx_ok(res.hash)
True
```
In the `prepare_exchange`, we ask Mike the seller to verify the transaction; and in the `finalize_exchange`, we ask Alice the buyer to verify the transaction. After both parties have verified, we can send the transaction directly.

Now if we check the laptop's owner, it should be Alice's address.

```python
rpc.get_single_asset_state(asset_address).owner == alice.wallet.address
True
```

Alice's account should have only 15 TBA after she pays for the laptop.

```python
>rpc.get_account_balance(alice.wallet.address)
150000000000000000
```

 🎉 🎉Congratulations! You have finished the Level 2 tutorial! Now you should have a general sense about how to create an asset and exchange assets with Forge SDK. Try and create more complicated assets!
