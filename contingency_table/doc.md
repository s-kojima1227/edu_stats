## 二元分割表

ex: 試験勉強の総時間 $T$ と合否 → 因子が２つ (総時間と合否) → "二元"分割表

| 試験勉強の総時間 $T$ | 合格 | 不合格 | 合計 |
|:--:|:-:|:-:|:-:|
| $T \ge 100$ 時間 | 68 | 14 | 82 |
| $T < 100$ 時間 | 26 | 92 | 118 |
| 合計 | 94 | 106 | 200 |

### 総度数が固定されていない場合

ex: 報道機関のニュース

|  | 政治 | 経済 | 合計 |
|:--:|:-:|:-:|:-:|
| 国内 | 74 | 66 | 140 |
| 海外 | 58 | 72 | 130 |
| 合計 | 132 | 138 | 270 |

→ セルごとに独立に非負整数値を取る\
→ 各セルが独立にポアソン分布としてモデリング

|  | 政治 | 経済 |
|:--:|:-:|:-:|
| 国内 | $\lambda_{11}$ | $\lambda_{12}$ |
| 海外 | $\lambda_{21}$ | $\lambda_{22}$ |

$$
\begin{align*}
&P(N_{11}=n_{11}, N_{12}=n_{12}, N_{21}=n_{21}, N_{22}=n_{22}) \\
&= \prod_{i=1, 2} \prod_{j=1, 2} \mathrm{Po}(\lambda_{ij}) \\
&= \prod_{i=1, 2} \prod_{j=1, 2} \frac{e^{-\lambda_{ij}} \cdot \lambda_{ij}^{n_{ij}}}{n_{ij}!}
\end{align*}
$$

### 総度数が固定されている場合

ex: 500個の製品のサンプリング

|  | 正常 | 不良 | 合計 |
|:--:|:-:|:-:|:-:|
| A | 276 | 16 | 292 |
| B | 196 | 12 | 208 |
| 合計 | 472 | 28 | 500 |

→ 各セルが独立にポアソン分布に従っているもとで, 総度数を固定する制約が与えられた条件付き分布としてモデリング

##### ■ 条件付き分布の導出

> 💡**POINT**\
>  $N_{ij} \sim \textrm{Po}(\lambda_{ij}) ~(i,j = 1,2)$ が独立のとき, $\sum_{i,j} N_{ij} \sim \textrm{Po}(\sum_{ij}\lambda_{ij})$

$$
\begin{align*}
&P(N_{11}=n_{11}, N_{12}=n_{12}, N_{21}=n_{21}, N_{22}=n_{22} | N_{11}+N_{12}+N_{21}+N_{22} = n) \\
&= \frac{
  P(N_{11}=n_{11}, N_{12}=n_{12}, N_{21}=n_{21}, N_{22}=n - (n_{11}+n_{12}+n_{21}))
 }{
  P(N_{11}+N_{12}+N_{21}+N_{22} = n)
 } \\
&= \frac{e^{-\lambda_{11}} \lambda_{11}^{n_{11}}}{n_{11}!} \cdot
   \frac{e^{-\lambda_{12}} \lambda_{12}^{n_{12}}}{n_{12}!} \cdot
   \frac{e^{-\lambda_{21}} \lambda_{21}^{n_{21}}}{n_{21}!} \cdot
   \frac{e^{-\lambda_{22}} \lambda_{22}^{n - (n_{11}+n_{12}+n_{21})}}{\{n - (n_{11}+n_{12}+n_{21})\}!} \cdot
   \frac{n!}{e^{-\lambda} \lambda^n} \\
&= \frac{n!}{n_{11}! \cdot n_{11}! \cdot n_{11}! \cdot \{n - (n_{11}+n_{12}+n_{21})\}!} \cdot
\Bigl( \frac{\lambda_{11}}{\lambda} \Bigl)^{n_{11}}
\Bigl( \frac{\lambda_{12}}{\lambda} \Bigl)^{n_{12}}
\Bigl( \frac{\lambda_{21}}{\lambda} \Bigl)^{n_{21}}
\Bigl( \frac{\lambda_{22}}{\lambda} \Bigl)^{n - (n_{11}+n_{12}+n_{21})} \\
&\sim M \Bigl(n;
  \frac{\lambda_{11}}{\lambda},
  \frac{\lambda_{12}}{\lambda},
  \frac{\lambda_{21}}{\lambda},
  \frac{\lambda_{22}}{\lambda}
  \Bigl)
\end{align*}
$$

つまり, 各セルが独立にポアソン分布に従っているもとで, 総度数を固定する制約が与えられた条件付き分布としてモデリングするということは, 多項分布に従うとモデリングすることと同じ意味になる.

そこで, 改めて多項分布でモデリングし直すと

$$
P(N_{11}=n_{11}, N_{12}=n_{12}, N_{21}=n_{21}, N_{22}=n_{22}) = 
\frac{(n_{11}+n_{11}+n_{11}+n_{22})!}{n_{11}! \cdot n_{11}! \cdot n_{11}! \cdot n_{22}!} \cdot
p_{11}^{n_{11}}
p_{12}^{n_{12}}
p_{21}^{n_{21}}
p_{22}^{n_{22}} \\
$$

### 行和 (または列和) が固定されている場合

ex: 資格対策講座AとBの受講後の成績の変化

|  | 上がった | 同程度 | 下がった | 合計 |
|:--:|:-:|:-:|:-:|:-:|
| A | 162 | 93 | 45 | 300 |
| B | 122 | 146 | 32 | 300 |
| 合計 | 284 | 239 | 77 | 600 |

→ 行ごとに独立な多項分布に従うとしてモデリング

### 行和と列和が固定されている場合

ex: AIが生成した絵7枚と画家の描いた絵3枚を見分ける

| 真実 \ 判定 | AI | 画家 | 合計 |
|:-:|:-:|:-:|:-:|
| AI  | 6  |  1  |  7  |
| 画家 | 1  |  2  |  3  |
| 合計 | 7  |  3  | 10  |

以下のような問題と本質的には同じ.

当たり(=画家)が3個, はずれ(=AI)が7個入った袋から7個取り出す.\
このうち, はずれが $k$ 個含まれる確率は

$$
P(X=k) = \frac{{}_7C_k \times {}_3C_{7-k}}{{}_{10}C_7}
$$

となる. このように, 各行を多項幾何分布に従うとしてモデリングする.

## カイ二乗適合度検定

### 前提

- $\boldsymbol \theta = (\theta_1, \theta_2, ..., \theta_m), ~\displaystyle \sum_{i=1}^m \theta_i = 1$
- $X = (X_1, X_2, ..., X_m) \sim M(n; \boldsymbol \theta)$ ; 多項分布

### 検定

- $\boldsymbol{\theta}_0 = (\theta_1^0, \theta_2^0, ..., \theta_m^0), ~\displaystyle \sum_{i=1}^m \theta_i^0 = 1$
- $H_0: \boldsymbol{\theta} = \boldsymbol{\theta}_0 ~~\textrm{v.s.}~~ H_1: \boldsymbol{\theta} \not= \boldsymbol{\theta}_0$

### 検定統計量

| | $1$ | $2$ | $\cdots$ | $m$ |
|:-:|:-:|:-:|:-:|:-:|
| 期待度数 | $n\theta_1^0$ | $n\theta_2^0$ | $\cdots$ | $n\theta_m^0$ |
| 観測度数 | $x_1$ | $x_2$ | $\cdots$ | $x_m$ |

$$
\sum_{i=1}^m \frac{(\textrm{観測度数}i - \textrm{期待度数}i)^2}{\textrm{期待度数}i}
= \sum_{i=1}^m \frac{(x_i - n\theta_i^0)^2}{n\theta_i^0}
\sim \chi^2(m-1)
$$

> 💡 $\displaystyle \sum_{i=1}^m \theta_i = 1$ という制約があるため, パラメータ $\boldsymbol{\theta}$ のうち自由に値を決められるパラメータの数は $m-1$ 個となる. したがって, 検定統計量の自由度は $m-1$ になっている.

## カイ二乗適合度検定 (具体例)

### 2×2分割表の各行の度数の合計を固定したモデル

##### ■ 例

ex: 資格対策講座AとBの受講後の成績の変化

|  | 上がった | 同程度 | 下がった | 合計 |
|:--:|:-:|:-:|:-:|:-:|
| A | 162 | 93 | 45 | 300 |
| B | 122 | 146 | 32 | 300 |
| 合計 | 284 | 239 | 77 | 600 |


##### ■ モデリング

各行に対して, 多項分布を仮定.

|  | 上がった | 同程度 | 下がった |
|:--:|:-:|:-:|:-:|
| A | $\theta_{11}$ | $\theta_{12}$ | $\theta_{13}$ |
| B | $\theta_{21}$ | $\theta_{22}$ | $\theta_{23}$ |


##### ■ 問題

資格対策講座AとBで成績の変化に差があるかを知りたい. つまり,
$$
H_0: \textrm{同じ列のパラメータは等しい}
~~\textrm{v.s.}~~
H_1: \textrm{同じ列のパラメータのうち, 等しくならないものが存在する}
$$

##### ■ 検定統計量の構成

| 観測度数表 | 上がった | 同程度 | 下がった | 合計 |
|:--:|:-:|:-:|:-:|:-:|
| A | $n_{11}$ | $n_{12}$ | $n_{13}$ | $n_{1\bullet}$ |
| B | $n_{21}$ | $n_{22}$ | $n_{23}$ | $n_{2\bullet}$ |
| 合計 | $n_{\bullet 1}$ | $n_{\bullet 2}$ | $n_{\bullet 3}$ | $n$ |

尤度を計算すると, 以下のようになる.

$$
\begin{align*}
L(\boldsymbol \theta) &= L_1(\boldsymbol\theta_{1\bullet}) \times L_2(\boldsymbol\theta_{2\bullet}) \\
&= \frac{n_1!}{n_{11}!n_{12}!n_{13}!}\theta_{11}^{n_{11}}\theta_{12}^{n_{12}}\theta_{13}^{n_{13}} \times \frac{n_2!}{n_{21}!n_{22}!n_{23}!}\theta_{21}^{n_{21}}\theta_{22}^{n_{22}}\theta_{23}^{n_{23}}\\
&= \frac{n_1!n_2!}{\prod_{i=1}^{2}\prod_{j=1}^{3}n_{ij}!}\prod_{i=1}^{2}\prod_{j=1}^{3}\theta_{ij}^{n_{ij}}
\end{align*}
$$

よって, 対数尤度は以下のようになる.

$$
l(\boldsymbol{\theta}) = \sum_{i=1}^2 \sum_{j=1}^3 n_{ij} \log\theta_{ij} + \textrm{const.}
$$

帰無仮説 ($\theta_{ij} \equiv \theta_j, ~\forall i$) の下では, 以下のようになる.

$$
l(\boldsymbol{\theta}) = \sum_{j=1}^3 n_{\bullet j} \log\theta_{j} + \textrm{const.}
$$

ラグランジュの未定乗数法を利用することで, 対数尤度 $l(\boldsymbol{\theta})$ を最大化するパラメータを求めると

$$
\theta_j = \frac{n_{\bullet j}}{n}, ~~\forall j=1,2,3
$$

となる.

| 観測度数 | 上がった | 同程度 | 下がった | 合計 |
|:--:|:-:|:-:|:-:|:-:|
| A | $n_{11}$ | $n_{12}$ | $n_{13}$ | $n_{1\bullet}$ |
| B | $n_{21}$ | $n_{22}$ | $n_{23}$ | $n_{2\bullet}$ |
| 合計 | $n_{\bullet 1}$ | $n_{\bullet 2}$ | $n_{\bullet 3}$ | $n$ |

| 期待度数 | 上がった | 同程度 | 下がった | 合計 |
|:--:|:-:|:-:|:-:|:-:|
| A | $\frac{n_{1\bullet} n_{\bullet 1}}{n}$ | $\frac{n_{1\bullet} n_{\bullet 2}}{n}$ | $\frac{n_{1\bullet} n_{\bullet 3}}{n}$ | $n_{1\bullet}$ |
| B | $\frac{n_{2\bullet} n_{\bullet 1}}{n}$ | $\frac{n_{2\bullet} n_{\bullet 2}}{n}$ | $\frac{n_{2\bullet} n_{\bullet 3}}{n}$ | $n_{2\bullet}$ |
| 合計 | $n_{\bullet 1}$ | $n_{\bullet 2}$ | $n_{\bullet 3}$ | $n$ |

適合度検定の検定統計量は、観測度数と期待度数の差の２乗を期待度数で割ったものの合計だから, 次のように表せる.

$$
\sum_{i=1}^{2} \sum_{j=1}^{3}
  \frac{
    \left(
      n_{ij} - \frac{n_{i.}n_{.j}}{n}
    \right)^2
  }{
    \frac{n_{i.}n_{.j}}{n}
  } \sim \chi^2(2)
$$

> 💡 帰無仮説の下では以下の制約があるため, 自由度は $2$ である.
> - $\theta_{11} + \theta_{12} + \theta_{13} = 1$
> - $\theta_{21} + \theta_{22} + \theta_{23} = 1$
> - $\theta_{11} = \theta_{21}$
> - $\theta_{12} = \theta_{22}$
> - $\theta_{13} = \theta_{23}$
>
> より一般に自由度は $(\textrm{行数 - 1}) \times (\textrm{列数 - 1})$ となる.

### 2×2分割表の総度数を固定したモデル

##### ■ 例

ex: 500個の製品のサンプリング

|  | 正常 | 不良 | 合計 |
|:--:|:-:|:-:|:-:|
| A | 276 | 16 | 292 |
| B | 196 | 12 | 208 |
| 合計 | 472 | 28 | 500 |

##### ■ モデリング

4項分布

|  | 正常 | 不良 | 合計 |
|:--:|:-:|:-:|:-:|
| A | $\theta_{11}$ | $\theta_{12}$ | $\theta_{1\bullet}$ |
| B | $\theta_{22}$ | $\theta_{21}$ | $\theta_{2\bullet}$ |
| 合計 | $\theta_{\bullet 1}$ | $\theta_{\bullet 2}$ | 1 |

##### ■ 問題

製造ラインAとBで不良品率に違いがあるのか？\
→ 行の因子と列の因子は独立であるか？

$$
H_0: \theta_{ij} = \theta_{i \bullet} \cdot \theta_{\bullet j}, ~~(i=1,2, j=1,2,3)
~~\textrm{v.s.}~~
H_1: H_0が成り立たない
$$

##### ■ 最尤推定量

| 観測度数 | 正常 | 不良 | 合計 |
|:--:|:-:|:-:|:-:|
| A | $n_{11}$ | $n_{12}$ | $n_{1\bullet}$ |
| B | $n_{22}$ | $n_{21}$ | $n_{2\bullet}$ |
| 合計 | $n_{\bullet 1}$ | $n_{\bullet 2}$ | $n$ |

| 最尤推定量 | 正常 | 不良 | 合計 |
|:--:|:-:|:-:|:-:|
| A | $\frac{n_{\bullet 1}}{n}\cdot\frac{n_{1\bullet}}{n}$ | $\frac{n_{\bullet 2}}{n}\cdot\frac{n_{1\bullet}}{n}$ | $\frac{n_{1\bullet}}{n}$ |
| B | $\frac{n_{\bullet 1}}{n}\cdot\frac{n_{2\bullet}}{n}$ | $\frac{n_{\bullet 2}}{n}\cdot\frac{n_{2\bullet}}{n}$ | $\frac{n_{2\bullet}}{n}$ |
| 合計 | $\frac{n_{\bullet 1}}{n}$ | $\frac{n_{\bullet 2}}{n}$ | $1$ |

##### ■ 検定統計量

$$
\sum_{i=1}^a \sum_{j=1}^b
  \frac{
    \left(
      n_{ij} - \frac{n_{i \bullet}}{n_{\bullet j}}
    \right)^2
  }{
    \frac{
      n_{i \bullet} n_{\bullet j}
    }{
      n
    }
  }
\sim \chi^2(ab-1)
$$
