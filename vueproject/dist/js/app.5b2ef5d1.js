(function(t){function e(e){for(var n,o,s=e[0],c=e[1],l=e[2],d=0,m=[];d<s.length;d++)o=s[d],Object.prototype.hasOwnProperty.call(i,o)&&i[o]&&m.push(i[o][0]),i[o]=0;for(n in c)Object.prototype.hasOwnProperty.call(c,n)&&(t[n]=c[n]);u&&u(e);while(m.length)m.shift()();return r.push.apply(r,l||[]),a()}function a(){for(var t,e=0;e<r.length;e++){for(var a=r[e],n=!0,s=1;s<a.length;s++){var c=a[s];0!==i[c]&&(n=!1)}n&&(r.splice(e--,1),t=o(o.s=a[0]))}return t}var n={},i={app:0},r=[];function o(e){if(n[e])return n[e].exports;var a=n[e]={i:e,l:!1,exports:{}};return t[e].call(a.exports,a,a.exports,o),a.l=!0,a.exports}o.m=t,o.c=n,o.d=function(t,e,a){o.o(t,e)||Object.defineProperty(t,e,{enumerable:!0,get:a})},o.r=function(t){"undefined"!==typeof Symbol&&Symbol.toStringTag&&Object.defineProperty(t,Symbol.toStringTag,{value:"Module"}),Object.defineProperty(t,"__esModule",{value:!0})},o.t=function(t,e){if(1&e&&(t=o(t)),8&e)return t;if(4&e&&"object"===typeof t&&t&&t.__esModule)return t;var a=Object.create(null);if(o.r(a),Object.defineProperty(a,"default",{enumerable:!0,value:t}),2&e&&"string"!=typeof t)for(var n in t)o.d(a,n,function(e){return t[e]}.bind(null,n));return a},o.n=function(t){var e=t&&t.__esModule?function(){return t["default"]}:function(){return t};return o.d(e,"a",e),e},o.o=function(t,e){return Object.prototype.hasOwnProperty.call(t,e)},o.p="/";var s=window["webpackJsonp"]=window["webpackJsonp"]||[],c=s.push.bind(s);s.push=e,s=s.slice();for(var l=0;l<s.length;l++)e(s[l]);var u=c;r.push([0,"chunk-vendors"]),a()})({0:function(t,e,a){t.exports=a("56d7")},"38f0":function(t,e,a){},"4c74":function(t,e,a){"use strict";var n=a("7679"),i=a.n(n);i.a},"56d7":function(t,e,a){"use strict";a.r(e);a("e260"),a("e6cf"),a("cca6"),a("a79d");var n=a("2b0e"),i=function(){var t=this,e=t.$createElement,a=t._self._c||e;return a("v-app",[a("Header"),a("router-view")],1)},r=[],o=function(){var t=this,e=t.$createElement,a=t._self._c||e;return a("v-card",{attrs:{color:"grey lighten-4",flat:"",tile:""}},[a("v-toolbar",{attrs:{dense:""}},[a("v-app-bar-nav-icon"),a("v-toolbar-title",{staticClass:"font-weight-bold"},[t._v("時間の達人")]),a("v-spacer"),a("v-btn",{attrs:{text:""}},[a("router-link",{attrs:{to:"/",tag:"button"}},[t._v("トップ")])],1),a("v-btn",{attrs:{text:""}},[a("router-link",{attrs:{to:"/top",tag:"button"}},[t._v("タスクの追加")])],1),a("v-btn",{attrs:{text:""}},[a("router-link",{attrs:{to:"/user",tag:"button"}},[t._v("秘密の設定")])],1)],1)],1)},s=[],c={},l=c,u=(a("d201"),a("2877")),d=a("6544"),m=a.n(d),f=a("5bc1"),h=a("8336"),v=a("b0af"),p=a("2fa4"),b=a("71d9"),k=a("2a7f"),x=Object(u["a"])(l,o,s,!1,null,"238101f9",null),g=x.exports;m()(x,{VAppBarNavIcon:f["a"],VBtn:h["a"],VCard:v["a"],VSpacer:p["a"],VToolbar:b["a"],VToolbarTitle:k["a"]});var T={name:"App",components:{Header:g},data:function(){return{}}},D=T,w=a("7496"),_=Object(u["a"])(D,i,r,!1,null,null,null),V=_.exports;m()(_,{VApp:w["a"]});var y=a("f309");n["a"].use(y["a"]);var C=new y["a"]({}),O=a("8c4f"),S=function(){var t=this,e=t.$createElement,n=t._self._c||e;return n("v-app",[n("v-container",{staticClass:"purple darken-4",attrs:{fluid:"","fill-height":""}},[n("v-row",{staticClass:"purple darken-4",staticStyle:{height:"450px"},attrs:{justify:"center","align-content":"center"}},[n("v-img",{attrs:{contain:"","max-height":"600","max-width":"600",src:a("692c")}}),n("v-col",[n("h1",{staticClass:"mb-10 font-weight-black white--text"},[t._v(" 自分を追い込むたった一つの方法 ")]),n("p",{staticClass:"mb-10 font-weight-black white--text"},[t._v(" 当サービスは、秘密を書き込み決められた時間にタスクが終わらな買った場合、強制的にTwitterに書き込まれるクレイジーでストイックなサービスです。 ")]),n("v-btn",{staticClass:"cyan accent-3 black--text font-weight-regular",attrs:{depressed:"",elevation:"15",raised:"",rounded:"","x-large":""},on:{click:function(e){return t.getCreateUrl()}}},[t._v("時間の達人になる")])],1)],1)],1)],1)},I=[],j={methods:{getCreateUrl:function(){location.href="https://google.com"}}},F=j,M=a("62ad"),$=a("a523"),E=a("adda"),Y=a("0fd9"),A=Object(u["a"])(F,S,I,!1,null,null,null),P=A.exports;m()(A,{VApp:w["a"],VBtn:h["a"],VCol:M["a"],VContainer:$["a"],VImg:E["a"],VRow:Y["a"]});var L=function(){var t=this,e=t.$createElement,a=t._self._c||e;return a("div",[a("TaskList")],1)},R=[],B=function(){var t=this,e=t.$createElement,a=t._self._c||e;return a("v-data-table",{staticClass:"elevation-1",attrs:{headers:t.headers,items:t.tasks,"sort-by":"limit"},scopedSlots:t._u([{key:"top",fn:function(){return[a("v-toolbar",{attrs:{flat:""}},[a("v-toolbar-title",[t._v("My CRUD")]),a("v-divider",{staticClass:"mx-4",attrs:{inset:"",vertical:""}}),a("v-spacer"),a("v-dialog",{attrs:{"max-width":"800px"},scopedSlots:t._u([{key:"activator",fn:function(e){var n=e.on,i=e.attrs;return[a("v-btn",t._g(t._b({staticClass:"mb-2",attrs:{color:"primary",dark:""}},"v-btn",i,!1),n),[t._v(" New Item ")])]}}]),model:{value:t.dialog,callback:function(e){t.dialog=e},expression:"dialog"}},[a("v-card",[a("v-card-title",[a("span",{staticClass:"headline"},[t._v(t._s(t.formTitle))])]),a("TaskForm",{ref:"taskform",on:{submitFromTaskForm:t.save,closeFromTaskForm:t.close,passTaskListAfterAddTask:t.updateTaskListAfterAddTask}})],1)],1),a("v-dialog",{attrs:{"max-width":"500px"},model:{value:t.dialogDelete,callback:function(e){t.dialogDelete=e},expression:"dialogDelete"}},[a("v-card",[a("v-card-title",{staticClass:"headline"},[t._v("このタスクを削除しますか？")]),a("v-form",{ref:"form",attrs:{"lazy-validation":""},model:{value:t.valid,callback:function(e){t.valid=e},expression:"valid"}},[a("v-checkbox",{attrs:{label:"タスク完了ツイートをする"},model:{value:t.checkbox,callback:function(e){t.checkbox=e},expression:"checkbox"}})],1),a("v-card-actions",[a("v-spacer"),a("v-btn",{attrs:{color:"blue darken-1",text:""},on:{click:t.closeDelete}},[t._v("キャンセル")]),a("v-btn",{attrs:{color:"blue darken-1",text:""},on:{click:t.deleteItemConfirm}},[t._v("OK")]),a("v-spacer")],1)],1)],1)],1)]},proxy:!0},{key:"item.actions",fn:function(e){var n=e.item;return[a("v-icon",{staticClass:"mr-2",attrs:{small:""},on:{click:function(e){return t.editItem(n)}}},[t._v(" mdi-pencil ")]),a("v-icon",{attrs:{small:""},on:{click:function(e){return t.deleteItem(n)}}},[t._v(" mdi-delete ")])]}},{key:"no-data",fn:function(){return[a("v-btn",{attrs:{color:"primary"},on:{click:t.initialize}},[t._v(" Reset ")])]},proxy:!0}])})},H=[],q=(a("99af"),a("4160"),a("c975"),a("fb6a"),a("a434"),a("b0c0"),a("4d90"),a("159b"),function(){var t=this,e=t.$createElement,a=t._self._c||e;return a("v-form",{ref:"form",attrs:{"lazy-validation":""},model:{value:t.valid,callback:function(e){t.valid=e},expression:"valid"}},[a("v-text-field",{attrs:{counter:100,rules:t.taskRules,label:"Task",required:""},model:{value:t.task,callback:function(e){t.task=e},expression:"task"}}),a("v-text-field",{attrs:{rules:t.emailRules,label:"E-mail",required:""},model:{value:t.email,callback:function(e){t.email=e},expression:"email"}}),a("DatePicker",{on:{passDateToParent:t.updateDate}}),a("TimePicker",{on:{passTimeToParent:t.updateTime}}),a("v-checkbox",{attrs:{label:"タスク着手のツイートをする"},model:{value:t.checkbox,callback:function(e){t.checkbox=e},expression:"checkbox"}}),a("v-btn",{staticClass:"mr-4",attrs:{disabled:!t.valid,color:"success"},on:{click:t.callSubmit}},[t._v(" Submit ")]),a("v-btn",{attrs:{color:"warning"},on:{click:t.callClose}},[t._v("Close")])],1)}),z=[],N=(a("ac1f"),a("5319"),function(){var t=this,e=t.$createElement,a=t._self._c||e;return a("v-container",[a("v-row",[a("v-col",{attrs:{cols:"12",lg:"6"}},[a("v-menu",{ref:"menu1",attrs:{"close-on-content-click":!1,transition:"scale-transition","offset-y":"","max-width":"290px","min-width":"290px"},scopedSlots:t._u([{key:"activator",fn:function(e){var n=e.on,i=e.attrs;return[a("v-text-field",t._g(t._b({attrs:{label:"Date",hint:"MM/DD/YYYY 形式","persistent-hint":"","prepend-icon":"mdi-calendar"},on:{blur:function(e){t.date=t.parseDate(t.dateFormatted)}},model:{value:t.dateFormatted,callback:function(e){t.dateFormatted=e},expression:"dateFormatted"}},"v-text-field",i,!1),n))]}}]),model:{value:t.menu1,callback:function(e){t.menu1=e},expression:"menu1"}},[a("v-date-picker",{attrs:{"no-title":""},on:{input:t.menu1ChangeAndEmit},model:{value:t.date,callback:function(e){t.date=e},expression:"date"}})],1)],1)],1)],1)}),U=[],J=(a("1276"),a("3835")),K={data:function(t){return{date:(new Date).toISOString().substr(0,10),dateFormatted:t.formatDate((new Date).toISOString().substr(0,10)),menu1:!1,menu2:!1}},computed:{computedDateFormatted:function(){return this.formatDate(this.date)}},watch:{date:{handler:function(){this.dateFormatted=this.formatDate(this.date)}}},methods:{formatDate:function(t){if(!t)return null;var e=t.split("-"),a=Object(J["a"])(e,3),n=a[0],i=a[1],r=a[2];return"".concat(i,"/").concat(r,"/").concat(n)},parseDate:function(t){if(!t)return null;var e=t.split("/"),a=Object(J["a"])(e,3),n=a[0],i=a[1],r=a[2];return"".concat(r,"-").concat(n.padStart(2,"0"),"-").concat(i.padStart(2,"0"))},formatDateYYYYMMDD:function(t){if(!t)return null;var e=t.split("/"),a=Object(J["a"])(e,3),n=a[0],i=a[1],r=a[2];return"".concat(r,"/").concat(n,"/").concat(i)},menu1ChangeAndEmit:function(){this.menu1=!1,this.changeDate()},changeDate:function(){this.$emit("passDateToParent",this.formatDateYYYYMMDD(this.dateFormatted))}}},G=K,Q=(a("4c74"),a("2e4b")),W=a("e449"),X=a("8654"),Z=Object(u["a"])(G,N,U,!1,null,"7a81b8bd",null),tt=Z.exports;m()(Z,{VCol:M["a"],VContainer:$["a"],VDatePicker:Q["a"],VMenu:W["a"],VRow:Y["a"],VTextField:X["a"]});var et=function(){var t=this,e=t.$createElement,a=t._self._c||e;return a("v-row",[a("v-col",{attrs:{cols:"11",sm:"5"}},[a("v-menu",{ref:"menu",attrs:{"close-on-content-click":!1,"nudge-right":40,"return-value":t.time,transition:"scale-transition","offset-y":"","max-width":"290px","min-width":"290px"},on:{"update:returnValue":function(e){t.time=e},"update:return-value":function(e){t.time=e}},scopedSlots:t._u([{key:"activator",fn:function(e){var n=e.on,i=e.attrs;return[a("v-text-field",t._g(t._b({attrs:{label:"Picker in menu","prepend-icon":"mdi-clock-time-four-outline",readonly:""},model:{value:t.time,callback:function(e){t.time=e},expression:"time"}},"v-text-field",i,!1),n))]}}]),model:{value:t.menu2,callback:function(e){t.menu2=e},expression:"menu2"}},[t.menu2?a("v-time-picker",{attrs:{"full-width":""},on:{"click:minute":function(e){return t.$refs.menu.save(t.time)},input:t.changeTime},model:{value:t.time,callback:function(e){t.time=e},expression:"time"}}):t._e()],1)],1)],1)},at=[],nt={data:function(){return{time:null,menu2:!1,modal2:!1}},created:function(){var t=new Date,e=t.getHours()+1,a=t.getMinutes();this.time="".concat(String(e).padStart(2,"0"),":").concat(String(a).padStart(2,"0"))},methods:{changeTime:function(){this.$emit("passTimeToParent",this.time)}}},it=nt,rt=a("c964"),ot=Object(u["a"])(it,et,at,!1,null,null,null),st=ot.exports;m()(ot,{VCol:M["a"],VMenu:W["a"],VRow:Y["a"],VTextField:X["a"],VTimePicker:rt["a"]});var ct=a("bc3a"),lt=a.n(ct),ut={components:{DatePicker:tt,TimePicker:st},data:function(){return{valid:!0,task:"",taskRules:[function(t){return!!t||"タスクは必須です"},function(t){return t&&t.length<=100||"タスクは100文字以内である必要があります"}],email:"",emailRules:[function(t){return!!t||"メールアドレスは必須です"},function(t){return/.+@.+\..+/.test(t)||"有効なメールアドレスを入力してください"}],checkbox:!1,date:null,time:"",responseTaskList:[]}},computed:{fullDate:function(){return new Date("".concat(this.date,"/").concat(this.time,":00"))},fullDateString:function(){return"".concat(this.date,"/").concat(this.time,":00")}},created:function(){var t=new Date,e=t.getHours()+1,a=t.getMinutes();this.time="".concat(String(e).padStart(2,"0"),":").concat(String(a).padStart(2,"0")),this.date=this.formatDate(new Date,"YYYY/MM/DD")},methods:{callSubmit:function(){this.$refs.form.validate()&&this.$emit("submitFromTaskForm")},reset:function(){this.$refs.form.reset()},callClose:function(){this.task="",this.email="",this.$refs.form.resetValidation(),this.$emit("closeFromTaskForm")},submit:function(){var t=this;lt.a.post("/task/create/add",{task:this.task,email:this.email,deadLine:this.fullDateString,tweet:this.checkbox,tweetedExpiredTask:0}).then((function(e){t.responseTaskList=e.data,t.passTaskListAfterAddTask(e.data)})),this.task="",this.email="",this.$refs.form.resetValidation()},updateDate:function(t){this.date=t},updateTime:function(t){this.time=t},formatDate:function(t,e){return e=e.replace(/YYYY/,t.getFullYear()),e=e.replace(/MM/,t.getMonth()+1),e=e.replace(/DD/,t.getDate()),e},passTaskListAfterAddTask:function(t){this.$emit("passTaskListAfterAddTask",t)}}},dt=ut,mt=a("ac7c"),ft=a("4bd4"),ht=Object(u["a"])(dt,q,z,!1,null,null,null),vt=ht.exports;m()(ht,{VBtn:h["a"],VCheckbox:mt["a"],VForm:ft["a"],VTextField:X["a"]});var pt=864e5,bt=36e5,kt=6e4,xt={components:{TaskForm:vt},data:function(){return{valid:!0,checkbox:!1,dialog:!1,dialogDelete:!1,headers:[{text:"ID",value:"id"},{text:"タスク",align:"start",sortable:!1,value:"name"},{text:"期限",value:"limit",sortable:!1},{text:"操作",value:"actions",sortable:!1}],editedIndex:-1,editedItem:{name:"",limit:0,id:""},defaultItem:{name:"",limit:0},now:new Date,taskData:[]}},created:function(){var t=this;lt.a.get("/json").then((function(e){e.data.forEach((function(e){t.tasks.push({name:e.name,limit:t.msToTime(new Date(e.deadLine)),id:e.id})}))})),this.sendOauthVerifier(this.$route.query.oauth_verifier),this.findExpiredTask()},computed:{formTitle:function(){return-1===this.editedIndex?"New Item":"Edit Item"},tasks:function(){return[{name:"課題",limit:this.msToTime(new Date("2020/10/16/12:30:00")),id:1},{name:"プログラミングする",limit:this.msToTime(new Date("2020/10/21/9:30:00")),id:2},{name:"ES提出",limit:this.msToTime(new Date("2020/10/21/11:22:00")),id:3},{name:"英単語100個",limit:this.msToTime(new Date("2020/10/21/17:00:00")),id:4},{name:"書類提出",limit:this.msToTime(new Date("2020/10/21/10:25:00")),id:5},{name:"ランニング10km",limit:this.msToTime(new Date("2020/10/21/9:40:00")),id:6},{name:"友達と遊ぶ",limit:this.msToTime(new Date("2020/10/21/22:00:30")),id:7}]}},watch:{dialog:function(t){t||this.close()},dialogDelete:function(t){t||this.closeDelete()},now:{handler:function(t){var e=this;t>0&&setTimeout((function(){e.now=new Date}),6e4)},immediate:!0}},methods:{editItem:function(t){this.editedIndex=this.tasks.indexOf(t),this.editedItem=Object.assign({},t),this.dialog=!0},deleteItem:function(t){var e=this;this.checkbox=!1,this.editedIndex=this.tasks.indexOf(t),this.editedItem=Object.assign({},t),this.dialogDelete=!0,lt.a.delete("/task/delete/".concat(t.id)).then((function(t){t.data.forEach((function(t){e.tasks=[],e.tasks.push({name:t.name,limit:e.msToTime(new Date(t.deadLine)),id:t.id})}))}))},deleteItemConfirm:function(){this.tasks.splice(this.editedIndex,1),this.checkbox&&console.log("Tweet task complete!"),this.closeDelete()},close:function(){var t=this;this.dialog=!1,this.$nextTick((function(){t.editedItem=Object.assign({},t.defaultItem),t.editedIndex=-1}))},closeDelete:function(){var t=this;this.dialogDelete=!1,this.$nextTick((function(){t.editedItem=Object.assign({},t.defaultItem),t.editedIndex=-1}))},save:function(){this.editedIndex>-1?Object.assign(this.tasks[this.editedIndex],this.editedItem):(this.tasks.push(this.editedItem),this.$refs.taskform.submit()),this.close()},msToTime:function(t){var e=t.getTime()-this.now.getTime();if(e<0)return"期限切れ";var a=Math.floor(e/pt),n=Math.floor((e-pt*a)/bt),i=Math.floor((e-pt*a-bt*n)/kt),r=("00"+n).slice(-2),o=("00"+i).slice(-2),s="".concat(String(a).padStart(2,"0"),"日").concat(r,"時").concat(o,"分");return s},findExpiredTask:function(){this.tasks.forEach((function(t){if("期限切れ"===t.limit){var e=t.id;console.log(e),lt.a.get("/task/".concat(e)).then((function(t){var a=t.data.tweetedExpiredTask;0===a&&lt.a.put("/task/update/".concat(e),{tweetedExpiredTask:1})}))}}))},sendOauthVerifier:function(t){var e=this;lt.a.post("link",{token:t}).then((function(t){e.taskData=t}))},updateTaskListAfterAddTask:function(t){var e=this;this.tasks=[],t.forEach((function(t){e.tasks.push({name:t.name,limit:e.msToTime(new Date(t.deadLine)),id:t.id})}))}}},gt=xt,Tt=(a("b085"),a("99d9")),Dt=a("8fea"),wt=a("169a"),_t=a("ce7e"),Vt=a("132d"),yt=Object(u["a"])(gt,B,H,!1,null,"9728c614",null),Ct=yt.exports;m()(yt,{VBtn:h["a"],VCard:v["a"],VCardActions:Tt["a"],VCardTitle:Tt["b"],VCheckbox:mt["a"],VDataTable:Dt["a"],VDialog:wt["a"],VDivider:_t["a"],VForm:ft["a"],VIcon:Vt["a"],VSpacer:p["a"],VToolbar:b["a"],VToolbarTitle:k["a"]});var Ot={components:{TaskList:Ct}},St=Ot,It=Object(u["a"])(St,L,R,!1,null,null,null),jt=It.exports,Ft=function(){var t=this,e=t.$createElement,a=t._self._c||e;return a("v-form",[a("v-container",{attrs:{fluid:"","fill-height":"",align:"center"}},[a("v-row",{attrs:{align:"center"}},[a("v-col",{attrs:{cols:"12",sm:"6"}},[a("v-text-field",{staticClass:"mb-10",attrs:{rules:t.rules,counter:"50",hint:"絶対誰にも言わないから",label:"とっておきの秘密を教えて！"},model:{value:t.secret_mess,callback:function(e){t.secret_mess=e},expression:"secret_mess"}}),a("v-btn",{attrs:{depressed:"",color:"primary"}},[t._v("これに決定！")])],1)],1)],1)],1)},Mt=[],$t={data:function(){return{secret_mess:"",rules:[function(t){return t.length<=50||"Max 50 characters"}]}}},Et=$t,Yt=Object(u["a"])(Et,Ft,Mt,!1,null,null,null),At=Yt.exports;m()(Yt,{VBtn:h["a"],VCol:M["a"],VContainer:$["a"],VForm:ft["a"],VRow:Y["a"],VTextField:X["a"]}),n["a"].use(O["a"]);var Pt=[{path:"/",component:P},{path:"/top",component:jt},{path:"/user",component:At}],Lt=new O["a"]({mode:"history",routes:Pt}),Rt=Lt,Bt=a("2f62");n["a"].use(Bt["a"]);var Ht=new Bt["a"].Store({state:{task:"",email:"",date:"",time:"",checkbox:""},getters:{},mutations:{changeTask:function(t,e){t.task=e}},actions:{}}),qt=Ht;n["a"].config.productionTip=!1,new n["a"]({vuetify:C,router:Rt,store:qt,render:function(t){return t(V)}}).$mount("#app")},"692c":function(t,e,a){t.exports=a.p+"img/top-image.e40af210.png"},7679:function(t,e,a){},b085:function(t,e,a){"use strict";var n=a("ce6d"),i=a.n(n);i.a},ce6d:function(t,e,a){},d201:function(t,e,a){"use strict";var n=a("38f0"),i=a.n(n);i.a}});
//# sourceMappingURL=app.5b2ef5d1.js.map