<?php
use yii\helpers\Html;
use yii\bootstrap\Nav;
use yii\bootstrap\NavBar;
use yii\widgets\Breadcrumbs;
use app\assets\AppAsset;

/**
 * @var \yii\web\View $this
 * @var string $content
 */
AppAsset::register($this);
?>
<?php $this->beginPage() ?>
<!DOCTYPE html>
<html lang="<?= Yii::$app->language ?>">
<head>
    <meta charset="<?= Yii::$app->charset ?>"/>
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title><?= Html::encode($this->title) ?></title>
    <?php $this->head() ?>
</head>
<body>

<?php $this->beginBody() ?>
    <div class="wrap">
        <?php
            NavBar::begin([
                'brandLabel' => 'Twitter-CCC',
                'brandUrl' => Yii::$app->homeUrl,
                'options' => [
                    'class' => 'navbar-inverse navbar-fixed-top',
                ],
            ]);
            echo Nav::widget([
                'options' => ['class' => 'navbar-nav navbar-right'],
                'items' => [
                    ['label' => 'Home', 'url' => ['/site/index']],
                    ['label' => 'About', 'url' => ['/site/about']],
                    // ['label' => 'About', 'url' => ['/site/about']],
                    ['label' => 'Melbourne', 'url' => ['/scenario/map?city=melbourne']
                    //     , 'items' => [
                    //     ['label'=> 'Heat map', 'url' =>['/scenario/map?city=melbourne']],
                    //     ['label'=> 'Mood by location', 'url' =>['/scenario/mood-location?city=melbourne']],
                    //     ['label'=> 'Time charts', 'url' =>['/scenario/time-charts?city=melbourne']],
                    // ]
                    ],
                    ['label' => 'Philadelphia', 'url'=> ['/scenario/map?city=philadelphia']
                    // , 'items' => [
                    //     ['label'=> 'Heat map', 'url' =>['/scenario/map?city=philadelphia']],
                    //     ['label'=> 'Mood by location', 'url' =>['/scenario/mood-location?city=philadelphia']],
                    //     ['label'=> 'Time charts', 'url' =>['/scenario/time-charts?city=philadelphia']],
                    // ]
                    ],
                    // Yii::$app->user->isGuest ?
                    //     ['label' => 'Login', 'url' => ['/site/login']] :
                    //     ['label' => 'Logout (' . Yii::$app->user->identity->username . ')',
                    //         'url' => ['/site/logout'],
                    //         'linkOptions' => ['data-method' => 'post']],
                ],
            ]);
            NavBar::end();
        ?>

        <div class="container">
            <?= Breadcrumbs::widget([
                'links' => isset($this->params['breadcrumbs']) ? $this->params['breadcrumbs'] : [],
            ]) ?>
            <?= $content ?>
        </div>
    </div>

    <footer class="footer">
        <div class="container">
            <p class="pull-left">&copy; Twitter-CCC <?= date('Y') ?></p>
            <p class="pull-right"><?= Yii::powered() ?></p>
        </div>
    </footer>

<?php $this->endBody() ?>
</body>
</html>
<?php $this->endPage() ?>
