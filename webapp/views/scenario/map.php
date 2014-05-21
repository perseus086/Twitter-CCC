    <script type="text/javascript">
      var requestUrl = "<?php echo $url; ?>";
      var bounds = "<?php echo $initialBounds; ?>";
      var city = "<?php echo $city; ?>";
      var mapCenter = [<?php echo $mapCenter; ?>];
      $(document).ready(function(){
        $('.charts-tabs a[data-toggle="tab"]').on('shown.bs.tab', function (e) {
          drawCharts();
        });
      });
    </script>
<div class="panel panel-default">
  <div class="panel-heading">Filters</div>
  <div class="panel-body">
    <h4><span class="label label-default">Data:</span></h4>
    <div class="btn-group type">
      <?php if($city == 'melbourne'){ ?>
        <button type="button" class="btn btn-default dropdown-toggle footy" data-toggle="dropdown">Footy<span class="caret"></span></button>
      <?php }else if($city == 'philadelphia'){ ?> 
        <button type="button" class="btn btn-default dropdown-toggle sports" data-toggle="dropdown">Sports<span class="caret"></span></button>
        <button type="button" class="btn btn-default rocky" value="rocky">Rocky</button>
      <?php } ?>
      <button type="button" class="btn btn-default popular" value="iamat">Check-in</button>
      <button type="button" class="btn btn-default popular" value="bar">Bars</button>
      <button type="button" class="btn btn-default popular" value="party">Parties</button>

      <button type="button" class="btn btn-default" value="positive">Happy</button>
      <button type="button" class="btn btn-default" value="negative">Sad</button>
      <button type="button" class="btn btn-default" value="all">All</button>
      <?php if($city == 'melbourne'){ ?>
        <ul class="dropdown-menu" role="menu">
          <li><a href="#" class="footy" value="all">All</a></li>
          <li><a href="#" class="footy" value="collingwood">Collingwood</a></li>
          <li><a href="#" class="footy" value="carlton">Carlton</a></li>
          <li><a href="#" class="footy" value="melbourne">Melbourne FC</a></li>
          <li><a href="#" class="footy" value="geelong">Geelong cats</a></li>
          <li><a href="#" class="footy" value="richmond">Richmond</a></li>
          <li><a href="#" class="footy" value="essendon">Essendon</a></li>
        </ul>
      <?php }else if($city == 'philadelphia'){ ?> 
        <ul class="dropdown-menu" role="menu">
          <li><a href="#" class="sports" value="all">All</a></li>
          <li><a href="#" class="sports" value="nba">NBA</a></li>
          <li><a href="#" class="sports" value="nfl">NFL</a></li>
          <li><a href="#" class="sports" value="mlb">Baseball</a></li>
        </ul>
      <?php } ?>

    </div>
    <span class="label label-info loader" style="display:none;">Loading...</span>
    <br/><br/>
    <h4><span class="label label-default">By time:</span></h4>
    <div class="btn-group">
      <button type="button" class="hour none btn btn-default" value="none">None</button>
      <?php
      for ($i=0; $i < 24; $i++) { ?>
      <button type="button" class="hour btn btn-default" value="<?php echo ($i < 10)?"0".$i:$i; ?>"><?php echo ($i < 10)?"0".$i:$i; ?></button>
      <?php }  ?>
    </div>
    <br/>
    <br/>
    <h4><span class="label label-default">By day:</span></h4>
    <div class="btn-group">
      <button type="button" class="day none btn btn-default" value="none">None</button>
      <?php
      foreach (array('Mon','Tue','Wed','Thu','Fri','Sat','Sun') as $key => $value) { ?>

      <button type="button" class="day btn btn-default" value="<?php echo $value; ?>"><?php echo $value; ?></button>
      <?php }  ?>
    </div><br/><br/>
    <h4><span class="label label-default">By lang:</span></h4>
    <div class="btn-group lang-list">
      <button type="button" class="lang none btn btn-default" value="none">None</button>
    </div><br/><br/>

    <h4><span class="label label-default">By mood:</span></h4>
    <div class="btn-group">
      <button type="button" class="mood none btn btn-default" value="none">None</button>
      <button type="button" class="mood btn btn-default" value="-100|-50">Sad [-100,-50]</button>
      <button type="button" class="mood btn btn-default" value="-50|-0.0001">[-50,0]</button>
      <button type="button" class="mood btn btn-default" value="0|0">[0,0]</button>
      <button type="button" class="mood btn btn-default" value="0.00001|50">[0,50]</button>
      <button type="button" class="mood btn btn-default" value="50|100">Happy [50,100]</button>
    </div>
  </div>
</div>

<div class="row">
  <div class="col-md-6">
    <div class="panel panel-default">
      <div class="panel-heading"><button type="button" class="btn-xs btn btn-default bounds-box pull-right">Show bounds box</button>Map</div>
      <div id="map-canvas" style="height:500px;"></div>
    </div>
    
    
  </div>
  <div class="col-md-6">

    <div class="panel panel-default">
      <div class="panel-heading">Tweets</div>
        <ul class="list-group tweets" style="overflow:auto; max-height:500px;">

        </ul>
    </div>
  </div>
</div>
<div class="panel panel-default">
  <div class="panel-heading">
    <div class="btn-group pull-right">
      <button type="button" id="pie-chart" class="btn-xs btn btn-default graph-type" status="">Pie charts</button>
      <button type="button" id="column-chart" class="btn-xs btn btn-default graph-type btn-success" status="show" >Column charts</button>
      <button type="button" id="data-table" class="btn-xs btn btn-default graph-type" status="">Show data</button>
    </div>
    Charts
  </div>
  <div class="charts-tabs">
  <!-- Nav tabs -->
      <ul class="nav nav-tabs">
        <li class="active"><a href="#day-tab" data-toggle="tab">By Day</a></li>
        <li><a href="#hour-tab" data-toggle="tab">By Hour</a></li>
        <li><a href="#lang-tab" data-toggle="tab">By Languages</a></li>
        <li><a href="#mood-tab" data-toggle="tab">By Mood</a></li>
        <li><a href="#mood-range-tab" data-toggle="tab">By Mood range</a></li>
      </ul>

      <!-- Tab panes -->
      <div class="tab-content">
        <div class="tab-pane active" id="day-tab">
          <div id="day-chart" ></div>
        </div>
        <div class="tab-pane" id="hour-tab">
          <div id="hour-chart" ></div>
        </div>
        <div class="tab-pane" id="lang-tab">
          <div class="checkbox">
            <label>
              <input type="checkbox" id="show-english" checked="checked">Show english
            </label>
          </div>
          <div id="lang-chart" ></div>
        </div>
        <div class="tab-pane" id="mood-range-tab">
          <div id="mood-range-chart" ></div>
        </div>
        <div class="tab-pane" id="mood-tab">
          <div id="mood-chart" ></div>
        </div>
      </div>  
  </div>
</div>
