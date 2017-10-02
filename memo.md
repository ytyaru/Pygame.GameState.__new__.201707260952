
* Mainクラスはpygameの骨組み（メインループ）
* StateSwitcherクラスはゲーム状態の管理と制御
* GameState系クラスはpygameのイベント処理と分岐
* GameCommandクラスはゲーム処理の実装


```python
SelectState.Initialize = GameCommand.NewGhostleg
SelectState.Finalize = クラス内実装
SelectState.Event = クラス内実装
SelectState.Draw = クラス内実装

AnimateState.Initialize = GameCommand.StartAnimation
AnimateState.Finalize = GameCommand.EndAnimation
AnimateState.Draw = GameCommand.Animation
AnimateState.Event = クラス内実装

ResultState.Initialize = GameCommand.StartGoalPerformance
ResultState.Finalize = GameCommand.EndGoalPerformance
ResultState.Event = クラス内実装
ResultState.Draw = GameCommand.GoalPerformance
```








# ゲームのコマンド

ゲームのコマンドとは、ゲーム固有のコマンドのことである。コマンドの内容は処理である。呼出元ではゲームコマンドの実行に必要なクラスや引数などを隠蔽したい。

## コマンド一覧

コマンド|説明
--------|----
あみだくじ新規作成|初回、結果表示からの再開のときに新しいあみだくじを作成する。
アニメーション開始|あみだくじで線を選択後、アニメーションを開始する。
アニメーション完了|アニメーション最中でも強制的に完了した状態にする。（座標の頂点リストを瞬時に完成させる）
結果演出開始|あみだくじのアニメーション完了後、効果音など何らかの演出をする。
結果演出終了|たとえば効果音などが鳴っている最中なら消す。

## 実行タイミング

ゲーム状態が変更された時に実行したい。各Stateクラスに以下のメソッドを実装させ、Switcherクラスで呼び出す。

* Initialize()
* Finalize()

## 共通クラス

* Screen
* CalcSize
* Ghostleg
* LinesAnimation

上記のような、各ゲームコマンドで利用するクラスをどう隠蔽するか。次回の課題。


```python
class CommonClasses:
    def __init__(self):
        self.__screen = Screen
        ...
    @property
    def Screeen(self): return self.__screen
    ...
```
```python
class GameCommand:
    def __init__(self):
        self.__common = CommonClasses
    def NewGhostleg(self):
        pass
    def StartAnimation(self):
        pass
    def EndAnimation(self):
        pass
    def StartGoalPerformance(self):
        pass
    def EndGoalPerformance(self):
        pass
```




















# ゲームのコマンド

ゲームのコマンドとは、ゲーム固有のコマンドのことである。

## 実装方法

デザインパターンのうちコマンドパターンを使ってはどうか。

すでにゲームの状態はStateパターンにて実装した。次は「状態」よりも細かい「コマンド」について実装したい。

## コマンド一覧

コマンド|説明
--------|----
あみだくじ新規作成|初回、結果表示からの再開のときに新しいあみだくじを作成する。
アニメーション開始|あみだくじで線を選択後、アニメーションを開始する。
結果演出|あみだくじのアニメーション完了後、効果音など何らかの演出をする。


## pythonにおけるデザパタ参考

* http://oneshotlife-python.hatenablog.com/entry/2016/03/21/225915
    * https://github.com/faif/python-patterns

