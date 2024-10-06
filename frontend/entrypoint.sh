#!/bin/bash
set -e

USERID=${LOCAL_USER_ID:-1000}
GROUPID=${LOCAL_GROUP_ID:-1000}

# nodeユーザーの名前をdcuserに変更
usermod -l dcuser -d /home/dcuser -m node
groupmod -n dcuser node

# 確認のため出力
echo "UserName: dcuser, UserID: $USERID, GroupID: $GROUPID"

# 一時的なグループを作成
groupadd -g 11111 tempgroup

# 「dcuser」ユーザーを一時的なグループにいったん所属させる
usermod -g tempgroup dcuser

# もともと所属していたdcuserグループを削除
groupdel dcuser

# ホストユーザーのGIDと同じGIDでdcuserグループを作成
groupadd -g $GROUPID dcuser

# dcuserユーザーのGIDをホストユーザーのGIDに設定
usermod -g $GROUPID dcuser

# dcuserユーザーのUIDをホストユーザーのUIDに設定
usermod -u $USERID dcuser

# 一時的なグループを削除
groupdel tempgroup

chown -R dcuser:dcuser /frontend

# 実行するコマンドを表示
echo "Executing command: $@"

exec "$@"
