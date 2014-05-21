<?php 

namespace app\controllers;

use Yii;
use yii\web\Controller;

class ScenarioController extends Controller
{

    public function beforeAction($action)
    {
        // echo "<pre>".print_r($action,true)."</pre>";
        switch($action->id){
            case 'map':
                Yii::$app->view->registerJsFile('https://maps.googleapis.com/maps/api/js?v=3.exp&sensor=false&libraries=visualization');
                Yii::$app->view->registerJsFile('https://www.google.com/jsapi');
                Yii::$app->view->registerJsFile('js/scenario/map.js');
            break;
            case 'mood-location':
                Yii::$app->view->registerJsFile('https://maps.googleapis.com/maps/api/js?v=3.exp&sensor=false&libraries=visualization');
                Yii::$app->view->registerJsFile('https://www.google.com/jsapi');
                Yii::$app->view->registerJsFile('js/scenario/mood_location.js');
            break;
            case 'time-charts':
                Yii::$app->view->registerJsFile('https://www.google.com/jsapi');
                Yii::$app->view->registerJsFile('js/scenario/time_charts.js');
            break;
        }

        return true;
    }

    // Actions
    public function actionMap($city)
    {
        // Yii::$app->view->registerJsFile('js/1.js');

        $url = null;
        $initialBounds = null;
        $customData = array();
        switch (strtolower($city)) {
            case 'melbourne':
                $url = 'http://115.146.94.20:5984/geomelbourne';
                $initialBounds = "144.3945,-38.2607,145.7647,-37.4598";
                $mapCenter = "-37.793472,144.995804";
            break;
            case 'philadelphia':
                $url = 'http://115.146.94.20:5984/geophiladelphia';
                $initialBounds = "-75.280303,39.867004,-74.955763,40.137992";
                $mapCenter = "39.9541995,-75.1638478,18";
                // file_get_contents("http://115.146.94.20:5984/geophiladelphia/_design/geo/_view/mood?key=\"all\"");
                // return "hola";
            break;
            
        }

        return $this->render('map',array(
            'city'=>$city,
            'url'=>$url,
            'initialBounds' => $initialBounds,
            'mapCenter'=>$mapCenter
        ));
    }

    public function actionMoodLocation($city){

        $url = null;
        switch (strtolower($city)) {
            case 'melbourne':
                $url = 'http://115.146.94.20:5984/geomelbourne';
            break;
        }

        return $this->render('mood_location',array(
            'city'=>$city,
            'url'=>$url,
        ));   
    }

      public function actionTimeCharts($city){

        $url = null;
        switch (strtolower($city)) {
            case 'melbourne':
                $url = 'http://115.146.94.20:5984/geomelbourne';
            break;
        }

        return $this->render('time_charts',array(
            'city'=>$city,
            'url'=>$url,
        ));      
    }

}