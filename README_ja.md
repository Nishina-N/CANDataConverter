# CANdata2matcsv

[![English](https://img.shields.io/badge/Language-English-blue)](README.md)
[![日本語](https://img.shields.io/badge/Language-日本語-red)](README_ja.md)

CAN（Controller Area Network）ログファイル（BLF、ASC）をDBCデータベースファイルを使用してCSVまたはMAT形式に変換するPythonベースのGUIツールです。

[![GitHub Sponsors](https://img.shields.io/github/sponsors/Nishina-N?style=social)](https://github.com/sponsors/Nishina-N)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python Version](https://img.shields.io/badge/python-3.7+-blue.svg)](https://www.python.org/downloads/)



<img width="484" height="485" alt="CANDataConverter" src="https://github.com/user-attachments/assets/f2745b5e-3a61-4e88-895b-35a00bf1a443" />



## 機能

- **対応入力形式**: BLF（Binary Logging Format）、ASC（ASCIIフォーマット）
- **対応出力形式**: CSV、MAT（MATLABフォーマット）
- **複数のリサンプリングオプション**:
  - 10ms周期リサンプリング
  - 100ms周期リサンプリング
  - 1秒周期リサンプリング
  - オリジナルサンプリング（各メッセージごとの個別時間軸）
- **GUIインターフェース**: 使いやすいtkinterベースのグラフィカルインターフェース
- **進捗表示**: 変換中のリアルタイム進捗バー
- **DBCサポート**: CANデータベースファイル（.dbc）を使用した信号デコード

## 必要要件

- Python 3.7以上
- 詳細な依存関係については`requirements.txt`を参照してください

## インストール

1. このリポジトリをクローン:
```bash
git clone https://github.com/yourusername/CANDataConverter.git
cd CANDataConverter
```

2. 必要なパッケージをインストール:
```bash
pip install -r requirements.txt
```

## 使用方法

1. メインスクリプトを実行:
```bash
python CANdata2matcsv.py
```

2. GUIでの操作:
   - CANデータベースファイル（.dbc）を選択
   - CANログファイル（.blfまたは.asc）を選択
   - 時間軸リサンプリングオプションを選択
   - 出力形式（CSVまたはMAT）を選択
   - 「Convert!」をクリック

3. 変換されたファイルは、入力ログファイルと同じディレクトリに、使用されたリサンプリング方法を示す適切なサフィックス付きで保存されます。

## ビルド済みバイナリのダウンロード

Windowsユーザーは、[リリース](https://github.com/Nishina-N/CANDataConverter/releases)ページからビルド済み実行ファイルをダウンロードできます。

## ファイル構造

```
CANDataConverter/
├── CANdata2matcsv.py      # メインGUIアプリケーション
├── CDW.py                 # CAN Data Wrapperクラス
├── tool/
│   ├── CAN_Extractor.py   # CANデータ抽出モジュール
│   └── CDW.py             # CAN Data Wrapper（ツール用コピー）
├── ico/                   # アイコンファイル（オプション）
├── LICENSE                # MITライセンス
├── README.md              # 英語版README
├── README_ja.md           # 日本語版README（このファイル）
└── requirements.txt       # Python依存関係
```

## 出力形式

### CSV形式
- リサンプリングデータ: 全信号が共通の時間軸に整列された単一CSV
- オリジナルサンプリング: メッセージごとの個別時間軸を持つ転置CSV

### MAT形式
- CAN IDごとに整理された信号グループを持つ構造化MATLABファイル
- 各CAN IDグループには信号と時間軸が含まれます

## このプロジェクトをサポート

このツールがお役に立った場合は、開発をサポートすることをご検討ください：

- ⭐ **このリポジトリにスター** - 他の人がこのツールを発見するのに役立ちます
- 💖 **[GitHubスポンサーになる](https://github.com/sponsors/Nishina-N)** - 継続的な開発をサポート
- 🐛 **バグを報告** - すべての人のためにツールを改善
- 🔧 **貢献** - プルリクエストを歓迎します！

あなたのサポートは、このツールの維持と改善に役立ちます。ありがとうございます！🙏

## ライセンス

このプロジェクトはMITライセンスの下でライセンスされています - 詳細は[LICENSE](LICENSE)ファイルをご覧ください。

### これが意味すること:
- ✅ **商用利用可能** - 制限なくビジネスで使用できます
- ✅ **改変可能** - ニーズに合わせて適応できます
- ✅ **配布可能** - 同僚や友人と共有できます
- ✅ **無保証** - 現状のまま提供されます

## 作者

**Nishina**
- 🌐 ウェブサイト: https://niseng.biz/software
- 💌 スポンサー: [GitHub Sponsors](https://github.com/sponsors/Nishina-N)
- © 2022-2026 Nishina

## 謝辞

- DBCパースには`cantools`ライブラリを使用
- CANログファイル読み込みには`python-can`ライブラリを使用
- CAN_ExtractorモジュールはLGPL v3ライセンスを使用

## バージョン履歴

- **v2.01** (2026): GitHubリリースバージョン - CAN_Extractor.exeをCAN_Extractor.pyに置き換え
- **v2.00**: 64ビット版
- **v1.05en**: 英語メッセージサポート
- **v1.05**: パフォーマンス改善、個別時間軸サポート
- **v1.04**: アイコン設定、UI改良
- **v1.03**: 特定のDBCファイルのバグ修正
- **v1.02**: ドットを含むファイル名のサポート
- **v1.01**: エラーメッセージの改善
- **v1.0**: 初回リリース

## 貢献

貢献を歓迎します！プルリクエストをお気軽に送信してください。ガイドラインについては[CONTRIBUTING.md](CONTRIBUTING.md)をご覧ください。

## サポートと問題

- 📖 **ドキュメント**: このREADME
- 🐛 **バグ報告**: [GitHub Issues](https://github.com/Nishina-N/CANDataConverter/issues)
- 💬 **質問**: [GitHub Discussions](https://github.com/Nishina-N/CANDataConverter/discussions)

---

<div align="center">

**このツールで時間を節約できた場合は、[スポンサーをご検討ください](https://github.com/sponsors/Nishina-N)**

Made by Nishina

</div>
