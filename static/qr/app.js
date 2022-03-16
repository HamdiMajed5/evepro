var app = new Vue({
  el: '#app',
  data: {
	delimiters: ["[[", "]]"],
    scanner: null,
    activeCameraId: null,
    cameras: [],
    scans: [],
	scanContent : []
  },
  mounted: function () {
    var self = this;
    self.scanner = new Instascan.Scanner({ video: document.getElementById('preview'), scanPeriod: 5 });
    self.scanner.addListener('scan', function (content, image) {
		if (self.scanContent.indexOf(self.conten) ===-1 ){
			play();
			self.scanContent.unshift(self.content);
			self.scans.unshift({ date: +(Date.now()), content: content });
			contentUrl=window.location.href + content
			if (ValidURL(contentUrl)){
				location.replace(contentUrl);};
			}
		else {
			alert ('Repeated');
		}
      //self.scans.unshift({ date: +(Date.now()), content: content });

    });
    Instascan.Camera.getCameras().then(function (cameras) {
      self.cameras = cameras;
      if (cameras.length > 0) {
        self.activeCameraId = cameras[0].id;
        self.scanner.start(cameras[0]);
      } else {
        console.error('No cameras found.');
      }
    }).catch(function (e) {
      console.error(e);
    });
  },
  methods: {
    formatName: function (name) {
      return name || '(unknown)';
    },
    selectCamera: function (camera) {
      this.activeCameraId = camera.id;
      this.scanner.start(camera);
    }
  }
});
function ValidURL(str) {
  var regex = /(http|https):\/\/(\w+:{0,1}\w*)?(\S+)(:[0-9]+)?(\/|\/([\w#!:.?+=&%!\-\/]))?/;
  if(!regex .test(str)) {
    alert("Please enter valid URL.");
    return false;
  } else {
    return true;
  }
}
function play(){
				//var audio = new Audio(window.location.origin+'/static/qr/succeeded-message-tone.mp3');
               // audio.play();
               var x = document.getElementById("myAudio");
               x.play();
}