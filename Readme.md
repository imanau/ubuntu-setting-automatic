# 概要

個人のUbuntuの設定自動化のためのansibleコードです。
過去の経験からUbuntuを壊してしまうことがあったため、いつ壊れても良いように自動化しています。

# 設定
- `xkeysnail`を利用してMacに近いキーバインドをできるようにします。

# テスト

いろいろ試したい場合は、同梱の`docker`を活用してコネコネしてください。

```bash
docker-comose build
docker-compose up -d
docker-compose exec ubuntu /bin/bash
# コンテナ内で
ansible-playbooky playbook.yml
```
