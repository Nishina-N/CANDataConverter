==========================================================================
CANDataConverter v2.02 - Windows バイナリ配布版
==========================================================================

これはCANDataConverterのビルド済みWindows実行ファイル版です。

## 内容物

- CANDataConverter.exe : メインアプリケーション (Windows 64ビット)
- ico/ : アイコンファイル
- LICENSE : ライセンス情報

## ソースコード

完全なソースコードは以下で入手可能です：
https://github.com/Nishina-N/CANDataConverter

## ライセンス情報

このソフトウェアは2つの異なるライセンスのコンポーネントで構成されています：

1. CANDataConverter (メインプログラム)
   - ライセンス: MIT License
   - Copyright (c) 2022-2026 Nishina
   - このソフトウェアは自由に使用、変更、配布できます。

2. CAN_Extractorモジュール (実行ファイルに含まれています)
   - ライセンス: GNU Lesser General Public License (LGPL) v3
   - ソースコードは上記のGitHubリポジトリで入手可能です。
   - このコンポーネントの取得、変更、再リンクの権利があります。

## 使用方法

1. CANDataConverter.exeをダブルクリックして実行
2. CANデータベースファイル（.dbc）を選択
3. CANログファイル（.blfまたは.asc）を選択
4. 出力形式と時間軸オプションを選択
5. 「Convert!」をクリック

## v2.02の新機能

- **データ整合性チェック**: 変換前にDBCファイルとBLFファイルのデータサイズ互換性を検証
- **デコードエラー処理**: 問題のあるメッセージを自動的にスキップし、処理を継続
- **エラーサマリー**: 変換後にデコードエラーの詳細レポートを表示
- **ユーザー確認**: 整合性の問題が検出された場合に確認を促す
- **UI改善**: プログレスインジケーターの強化と、より明確な警告メッセージ

## システム要件

- Windows 10/11 (64ビット)
- Pythonのインストールは不要

## サポート

問題、質問、機能リクエストについては：
- GitHub Issues: https://github.com/Nishina-N/CANDataConverter/issues
- ウェブサイト: https://niseng.biz/software

このツールが役に立った場合は、ぜひご検討ください：
- GitHubリポジトリにスターを付ける
- GitHubスポンサーになる: https://github.com/sponsors/Nishina-N

## 著作権

Copyright (c) 2022-2026 Nishina

==========================================================================
