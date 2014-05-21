<?php 

namespace app\controllers;

use Yii;
use yii\web\Controller;

class ApiController extends Controller
{
    private $format = 'json';

    public function beforeAction($action)
    {
        Yii::$app->response->format = 'json';
        return true;
    }

    public function actionList($city,$type,$polarity = null,$limit = null)
    {

        // $city = Yii::$app->request->get('city');
        // $type = Yii::$app->request->get('type');
        // $polarity = Yii::$app->request->get('polarity');

        return $this->getCouchDBRequest($city,'api',$type,$polarity,array('limit'=>$limit));
    }

    private function getCouchDBRequest($city,$view,$type,$polarity = null,$couchDBParams)
    {
        $baseUrl = "";
        switch ($city) {
            case 'melbourne':
                $baseUrl = "http://115.146.94.20:5984/geomelbourne";
            break;
            case 'philadelphia':
                $baseUrl = "http://115.146.94.20:5984/geophiladelphia";
            break;
            
            default:
            break;
        }
        $url = $baseUrl."/_design/rest/_view/".$view;
        $polarityStart = ($polarity == null)?'""':('"'.$polarity.'"');
        $polarityEnd = ($polarity == null)?'{}':('"'.$polarity.'"');
        $startKey = '["'.$type.'",'.$polarityStart."]";
        $endKey = '["'.$type.'",'.$polarityEnd."]";

        $url = $url.'?'.http_build_query(array(
            'limit'=>$couchDBParams['limit'],
            'startkey'=> $startKey,
            'endkey'=>$endKey
        ));

        return json_decode(file_get_contents($url));
    }
    
    public function actionView()
    {
    }
    public function actionCreate()
    {
    }
    public function actionUpdate()
    {
    }
    public function actionDelete()
    {
    }
}