<html><head><meta http-equiv="Content-Type" content="text/html; charset=utf-8"/><title>Shopping - Store </title><style>
/* cspell:disable-file */
/* webkit printing magic: print all background colors */
html {
	-webkit-print-color-adjust: exact;
}
* {
	box-sizing: border-box;
	-webkit-print-color-adjust: exact;
}

html,
body {
	margin: 0;git 
	padding: 0;
}
@media only screen {
	body {
		margin: 2em auto;
		max-width: 900px;
		color: rgb(55, 53, 47);
	}
}

body {
	line-height: 1.5;
	white-space: pre-wrap;
}

a,
a.visited {
	color: inherit;
	text-decoration: underline;
}

.pdf-relative-link-path {
	font-size: 80%;
	color: #444;
}

h1,
h2,
h3 {
	letter-spacing: -0.01em;
	line-height: 1.2;
	font-weight: 600;
	margin-bottom: 0;
}

.page-title {
	font-size: 2.5rem;
	font-weight: 700;
	margin-top: 0;
	margin-bottom: 0.75em;
}

h1 {
	font-size: 1.875rem;
	margin-top: 1.875rem;
}

h2 {
	font-size: 1.5rem;
	margin-top: 1.5rem;
}

h3 {
	font-size: 1.25rem;
	margin-top: 1.25rem;
}

.source {
	border: 1px solid #ddd;
	border-radius: 3px;
	padding: 1.5em;
	word-break: break-all;
}

.callout {
	border-radius: 3px;
	padding: 1rem;
}

figure {
	margin: 1.25em 0;
	page-break-inside: avoid;
}

figcaption {
	opacity: 0.5;
	font-size: 85%;
	margin-top: 0.5em;
}

mark {
	background-color: transparent;
}

.indented {
	padding-left: 1.5em;
}

hr {
	background: transparent;
	display: block;
	width: 100%;
	height: 1px;
	visibility: visible;
	border: none;
	border-bottom: 1px solid rgba(55, 53, 47, 0.09);
}

img {
	max-width: 100%;
}

@media only print {
	img {
		max-height: 100vh;
		object-fit: contain;
	}
}

@page {
	margin: 1in;
}

.collection-content {
	font-size: 0.875rem;
}

.column-list {
	display: flex;
	justify-content: space-between;
}

.column {
	padding: 0 1em;
}

.column:first-child {
	padding-left: 0;
}

.column:last-child {
	padding-right: 0;
}

.table_of_contents-item {
	display: block;
	font-size: 0.875rem;
	line-height: 1.3;
	padding: 0.125rem;
}

.table_of_contents-indent-1 {
	margin-left: 1.5rem;
}

.table_of_contents-indent-2 {
	margin-left: 3rem;
}

.table_of_contents-indent-3 {
	margin-left: 4.5rem;
}

.table_of_contents-link {
	text-decoration: none;
	opacity: 0.7;
	border-bottom: 1px solid rgba(55, 53, 47, 0.18);
}

table,
th,
td {
	border: 1px solid rgba(55, 53, 47, 0.09);
	border-collapse: collapse;
}

table {
	border-left: none;
	border-right: none;
}

th,
td {
	font-weight: normal;
	padding: 0.25em 0.5em;
	line-height: 1.5;
	min-height: 1.5em;
	text-align: left;
}

th {
	color: rgba(55, 53, 47, 0.6);
}

ol,
ul {
	margin: 0;
	margin-block-start: 0.6em;
	margin-block-end: 0.6em;
}

li > ol:first-child,
li > ul:first-child {
	margin-block-start: 0.6em;
}

ul > li {
	list-style: disc;
}

ul.to-do-list {
	text-indent: -1.7em;
}

ul.to-do-list > li {
	list-style: none;
}

.to-do-children-checked {
	text-decoration: line-through;
	opacity: 0.375;
}

ul.toggle > li {
	list-style: none;
}

ul {
	padding-inline-start: 1.7em;
}

ul > li {
	padding-left: 0.1em;
}

ol {
	padding-inline-start: 1.6em;
}

ol > li {
	padding-left: 0.2em;
}

.mono ol {
	padding-inline-start: 2em;
}

.mono ol > li {
	text-indent: -0.4em;
}

.toggle {
	padding-inline-start: 0em;
	list-style-type: none;
}

/* Indent toggle children */
.toggle > li > details {
	padding-left: 1.7em;
}

.toggle > li > details > summary {
	margin-left: -1.1em;
}

.selected-value {
	display: inline-block;
	padding: 0 0.5em;
	background: rgba(206, 205, 202, 0.5);
	border-radius: 3px;
	margin-right: 0.5em;
	margin-top: 0.3em;
	margin-bottom: 0.3em;
	white-space: nowrap;
}

.collection-title {
	display: inline-block;
	margin-right: 1em;
}

time {
	opacity: 0.5;
}

.icon {
	display: inline-block;
	max-width: 1.2em;
	max-height: 1.2em;
	text-decoration: none;
	vertical-align: text-bottom;
	margin-right: 0.5em;
}

img.icon {
	border-radius: 3px;
}

.user-icon {
	width: 1.5em;
	height: 1.5em;
	border-radius: 100%;
	margin-right: 0.5rem;
}

.user-icon-inner {
	font-size: 0.8em;
}

.text-icon {
	border: 1px solid #000;
	text-align: center;
}

.page-cover-image {
	display: block;
	object-fit: cover;
	width: 100%;
	height: 30vh;
}

.page-header-icon {
	font-size: 3rem;
	margin-bottom: 1rem;
}

.page-header-icon-with-cover {
	margin-top: -0.72em;
	margin-left: 0.07em;
}

.page-header-icon img {
	border-radius: 3px;
}

.link-to-page {
	margin: 1em 0;
	padding: 0;
	border: none;
	font-weight: 500;
}

p > .user {
	opacity: 0.5;
}

td > .user,
td > time {
	white-space: nowrap;
}

input[type="checkbox"] {
	transform: scale(1.5);
	margin-right: 0.6em;
	vertical-align: middle;
}

p {
	margin-top: 0.5em;
	margin-bottom: 0.5em;
}

.image {
	border: none;
	margin: 1.5em 0;
	padding: 0;
	border-radius: 0;
	text-align: center;
}

.code,
code {
	background: rgba(135, 131, 120, 0.15);
	border-radius: 3px;
	padding: 0.2em 0.4em;
	border-radius: 3px;
	font-size: 85%;
	tab-size: 2;
}

code {
	color: #eb5757;
}

.code {
	padding: 1.5em 1em;
}

.code-wrap {
	white-space: pre-wrap;
	word-break: break-all;
}

.code > code {
	background: none;
	padding: 0;
	font-size: 100%;
	color: inherit;
}

blockquote {
	font-size: 1.25em;
	margin: 1em 0;
	padding-left: 1em;
	border-left: 3px solid rgb(55, 53, 47);
}

.bookmark {
	text-decoration: none;
	max-height: 8em;
	padding: 0;
	display: flex;
	width: 100%;
	align-items: stretch;
}

.bookmark-title {
	font-size: 0.85em;
	overflow: hidden;
	text-overflow: ellipsis;
	height: 1.75em;
	white-space: nowrap;
}

.bookmark-text {
	display: flex;
	flex-direction: column;
}

.bookmark-info {
	flex: 4 1 180px;
	padding: 12px 14px 14px;
	display: flex;
	flex-direction: column;
	justify-content: space-between;
}

.bookmark-image {
	width: 33%;
	flex: 1 1 180px;
	display: block;
	position: relative;
	object-fit: cover;
	border-radius: 1px;
}

.bookmark-description {
	color: rgba(55, 53, 47, 0.6);
	font-size: 0.75em;
	overflow: hidden;
	max-height: 4.5em;
	word-break: break-word;
}

.bookmark-href {
	font-size: 0.75em;
	margin-top: 0.25em;
}

.sans { font-family: ui-sans-serif, -apple-system, BlinkMacSystemFont, "Segoe UI", Helvetica, "Apple Color Emoji", Arial, sans-serif, "Segoe UI Emoji", "Segoe UI Symbol"; }
.code { font-family: "SFMono-Regular", Menlo, Consolas, "PT Mono", "Liberation Mono", Courier, monospace; }
.serif { font-family: Lyon-Text, Georgia, ui-serif, serif; }
.mono { font-family: iawriter-mono, Nitti, Menlo, Courier, monospace; }
.pdf .sans { font-family: Inter, ui-sans-serif, -apple-system, BlinkMacSystemFont, "Segoe UI", Helvetica, "Apple Color Emoji", Arial, sans-serif, "Segoe UI Emoji", "Segoe UI Symbol", 'Twemoji', 'Noto Color Emoji', 'Noto Sans CJK JP'; }
.pdf:lang(zh-CN) .sans { font-family: Inter, ui-sans-serif, -apple-system, BlinkMacSystemFont, "Segoe UI", Helvetica, "Apple Color Emoji", Arial, sans-serif, "Segoe UI Emoji", "Segoe UI Symbol", 'Twemoji', 'Noto Color Emoji', 'Noto Sans CJK SC'; }
.pdf:lang(zh-TW) .sans { font-family: Inter, ui-sans-serif, -apple-system, BlinkMacSystemFont, "Segoe UI", Helvetica, "Apple Color Emoji", Arial, sans-serif, "Segoe UI Emoji", "Segoe UI Symbol", 'Twemoji', 'Noto Color Emoji', 'Noto Sans CJK TC'; }
.pdf:lang(ko-KR) .sans { font-family: Inter, ui-sans-serif, -apple-system, BlinkMacSystemFont, "Segoe UI", Helvetica, "Apple Color Emoji", Arial, sans-serif, "Segoe UI Emoji", "Segoe UI Symbol", 'Twemoji', 'Noto Color Emoji', 'Noto Sans CJK KR'; }
.pdf .code { font-family: Source Code Pro, "SFMono-Regular", Menlo, Consolas, "PT Mono", "Liberation Mono", Courier, monospace, 'Twemoji', 'Noto Color Emoji', 'Noto Sans Mono CJK JP'; }
.pdf:lang(zh-CN) .code { font-family: Source Code Pro, "SFMono-Regular", Menlo, Consolas, "PT Mono", "Liberation Mono", Courier, monospace, 'Twemoji', 'Noto Color Emoji', 'Noto Sans Mono CJK SC'; }
.pdf:lang(zh-TW) .code { font-family: Source Code Pro, "SFMono-Regular", Menlo, Consolas, "PT Mono", "Liberation Mono", Courier, monospace, 'Twemoji', 'Noto Color Emoji', 'Noto Sans Mono CJK TC'; }
.pdf:lang(ko-KR) .code { font-family: Source Code Pro, "SFMono-Regular", Menlo, Consolas, "PT Mono", "Liberation Mono", Courier, monospace, 'Twemoji', 'Noto Color Emoji', 'Noto Sans Mono CJK KR'; }
.pdf .serif { font-family: PT Serif, Lyon-Text, Georgia, ui-serif, serif, 'Twemoji', 'Noto Color Emoji', 'Noto Serif CJK JP'; }
.pdf:lang(zh-CN) .serif { font-family: PT Serif, Lyon-Text, Georgia, ui-serif, serif, 'Twemoji', 'Noto Color Emoji', 'Noto Serif CJK SC'; }
.pdf:lang(zh-TW) .serif { font-family: PT Serif, Lyon-Text, Georgia, ui-serif, serif, 'Twemoji', 'Noto Color Emoji', 'Noto Serif CJK TC'; }
.pdf:lang(ko-KR) .serif { font-family: PT Serif, Lyon-Text, Georgia, ui-serif, serif, 'Twemoji', 'Noto Color Emoji', 'Noto Serif CJK KR'; }
.pdf .mono { font-family: PT Mono, iawriter-mono, Nitti, Menlo, Courier, monospace, 'Twemoji', 'Noto Color Emoji', 'Noto Sans Mono CJK JP'; }
.pdf:lang(zh-CN) .mono { font-family: PT Mono, iawriter-mono, Nitti, Menlo, Courier, monospace, 'Twemoji', 'Noto Color Emoji', 'Noto Sans Mono CJK SC'; }
.pdf:lang(zh-TW) .mono { font-family: PT Mono, iawriter-mono, Nitti, Menlo, Courier, monospace, 'Twemoji', 'Noto Color Emoji', 'Noto Sans Mono CJK TC'; }
.pdf:lang(ko-KR) .mono { font-family: PT Mono, iawriter-mono, Nitti, Menlo, Courier, monospace, 'Twemoji', 'Noto Color Emoji', 'Noto Sans Mono CJK KR'; }
.highlight-default {
	color: rgba(55, 53, 47, 1);
}
.highlight-gray {
	color: rgba(120, 119, 116, 1);
	fill: rgba(145, 145, 142, 1);
}
.highlight-brown {
	color: rgba(159, 107, 83, 1);
	fill: rgba(187, 132, 108, 1);
}
.highlight-orange {
	color: rgba(217, 115, 13, 1);
	fill: rgba(215, 129, 58, 1);
}
.highlight-yellow {
	color: rgba(203, 145, 47, 1);
	fill: rgba(203, 148, 51, 1);
}
.highlight-teal {
	color: rgba(68, 131, 97, 1);
	fill: rgba(108, 155, 125, 1);
}
.highlight-blue {
	color: rgba(51, 126, 169, 1);
	fill: rgba(91, 151, 189, 1);
}
.highlight-purple {
	color: rgba(144, 101, 176, 1);
	fill: rgba(167, 130, 195, 1);
}
.highlight-pink {
	color: rgba(193, 76, 138, 1);
	fill: rgba(205, 116, 159, 1);
}
.highlight-red {
	color: rgba(212, 76, 71, 1);
	fill: rgba(225, 111, 100, 1);
}
.highlight-gray_background {
	background: rgba(241, 241, 239, 1);
}
.highlight-brown_background {
	background: rgba(244, 238, 238, 1);
}
.highlight-orange_background {
	background: rgba(251, 236, 221, 1);
}
.highlight-yellow_background {
	background: rgba(251, 243, 219, 1);
}
.highlight-teal_background {
	background: rgba(237, 243, 236, 1);
}
.highlight-blue_background {
	background: rgba(231, 243, 248, 1);
}
.highlight-purple_background {
	background: rgba(244, 240, 247, 0.8);
}
.highlight-pink_background {
	background: rgba(249, 238, 243, 0.8);
}
.highlight-red_background {
	background: rgba(253, 235, 236, 1);
}
.block-color-default {
	color: inherit;
	fill: inherit;
}
.block-color-gray {
	color: rgba(120, 119, 116, 1);
	fill: rgba(145, 145, 142, 1);
}
.block-color-brown {
	color: rgba(159, 107, 83, 1);
	fill: rgba(187, 132, 108, 1);
}
.block-color-orange {
	color: rgba(217, 115, 13, 1);
	fill: rgba(215, 129, 58, 1);
}
.block-color-yellow {
	color: rgba(203, 145, 47, 1);
	fill: rgba(203, 148, 51, 1);
}
.block-color-teal {
	color: rgba(68, 131, 97, 1);
	fill: rgba(108, 155, 125, 1);
}
.block-color-blue {
	color: rgba(51, 126, 169, 1);
	fill: rgba(91, 151, 189, 1);
}
.block-color-purple {
	color: rgba(144, 101, 176, 1);
	fill: rgba(167, 130, 195, 1);
}
.block-color-pink {
	color: rgba(193, 76, 138, 1);
	fill: rgba(205, 116, 159, 1);
}
.block-color-red {
	color: rgba(212, 76, 71, 1);
	fill: rgba(225, 111, 100, 1);
}
.block-color-gray_background {
	background: rgba(241, 241, 239, 1);
}
.block-color-brown_background {
	background: rgba(244, 238, 238, 1);
}
.block-color-orange_background {
	background: rgba(251, 236, 221, 1);
}
.block-color-yellow_background {
	background: rgba(251, 243, 219, 1);
}
.block-color-teal_background {
	background: rgba(237, 243, 236, 1);
}
.block-color-blue_background {
	background: rgba(231, 243, 248, 1);
}
.block-color-purple_background {
	background: rgba(244, 240, 247, 0.8);
}
.block-color-pink_background {
	background: rgba(249, 238, 243, 0.8);
}
.block-color-red_background {
	background: rgba(253, 235, 236, 1);
}
.select-value-color-pink { background-color: rgba(245, 224, 233, 1); }
.select-value-color-purple { background-color: rgba(232, 222, 238, 1); }
.select-value-color-green { background-color: rgba(219, 237, 219, 1); }
.select-value-color-gray { background-color: rgba(227, 226, 224, 1); }
.select-value-color-orange { background-color: rgba(250, 222, 201, 1); }
.select-value-color-brown { background-color: rgba(238, 224, 218, 1); }
.select-value-color-red { background-color: rgba(255, 226, 221, 1); }
.select-value-color-yellow { background-color: rgba(253, 236, 200, 1); }
.select-value-color-blue { background-color: rgba(211, 229, 239, 1); }

.checkbox {
	display: inline-flex;
	vertical-align: text-bottom;
	width: 16;
	height: 16;
	background-size: 16px;
	margin-left: 2px;
	margin-right: 5px;
}

.checkbox-on {
	background-image: url("data:image/svg+xml;charset=UTF-8,%3Csvg%20width%3D%2216%22%20height%3D%2216%22%20viewBox%3D%220%200%2016%2016%22%20fill%3D%22none%22%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%3E%0A%3Crect%20width%3D%2216%22%20height%3D%2216%22%20fill%3D%22%2358A9D7%22%2F%3E%0A%3Cpath%20d%3D%22M6.71429%2012.2852L14%204.9995L12.7143%203.71436L6.71429%209.71378L3.28571%206.2831L2%207.57092L6.71429%2012.2852Z%22%20fill%3D%22white%22%2F%3E%0A%3C%2Fsvg%3E");
}

.checkbox-off {
	background-image: url("data:image/svg+xml;charset=UTF-8,%3Csvg%20width%3D%2216%22%20height%3D%2216%22%20viewBox%3D%220%200%2016%2016%22%20fill%3D%22none%22%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%3E%0A%3Crect%20x%3D%220.75%22%20y%3D%220.75%22%20width%3D%2214.5%22%20height%3D%2214.5%22%20fill%3D%22white%22%20stroke%3D%22%2336352F%22%20stroke-width%3D%221.5%22%2F%3E%0A%3C%2Fsvg%3E");
}
	
</style></head><body><article id="decbb42a-e529-4819-9148-10e1e36dabd2" class="page sans"><header><h1 class="page-title">Shopping - Store </h1></header><div class="page-body"><h2 id="63691b24-9811-49b7-a0b0-2b4c9d4425c7" class="">End Points </h2><ul id="a92346d3-15da-442d-aae9-2b83df6aff77" class="bulleted-list"><li style="list-style-type:disc">GET  /   redirect to login page  </li></ul><ul id="91284f25-bb70-47b2-a982-232ff1827b59" class="bulleted-list"><li style="list-style-type:disc">GET /login     login using auth0 </li></ul><ul id="541aa100-0913-42e8-9402-5455ebae0694" class="bulleted-list"><li style="list-style-type:disc">GET /logout  logout using auth0</li></ul><ul id="d84ec93a-2909-423d-982c-e3300a7c8944" class="bulleted-list"><li style="list-style-type:disc">GET /products get all products /</li></ul><ul id="3baa1657-b911-47a0-a920-decafc2a3f5e" class="bulleted-list"><li style="list-style-type:disc"> GET /products/&lt;int:product_id&gt; </li></ul><ul id="cf473e6b-fd0e-4c99-a211-850b66f1f3d0" class="bulleted-list"><li style="list-style-type:disc"> GET /customers/&lt;int:customer_id      </li></ul><ul id="4c2eb2ca-3ae0-4263-81a7-5e4f50cae598" class="bulleted-list"><li style="list-style-type:disc">GET  /customers/int:customer_id/items   gets cart item for a user</li></ul><ul id="22c1dad8-099c-4520-94e8-03e03a1b3127" class="bulleted-list"><li style="list-style-type:disc">GET /categories </li></ul><ul id="fc2cb912-2d1a-438c-b994-c96d39c7a7a4" class="bulleted-list"><li style="list-style-type:disc">POST /item</li></ul><ul id="3e044dbe-1f92-4f3d-a7d9-bf534215a97c" class="bulleted-list"><li style="list-style-type:disc">POST  /product</li></ul><ul id="9f71826e-8cf4-461e-81bb-01d30c0a4677" class="bulleted-list"><li style="list-style-type:disc">POST  /category</li></ul><ul id="0923fe12-44b6-4fe7-8794-15f7e63bc719" class="bulleted-list"><li style="list-style-type:disc">POST  /customer</li></ul><ul id="02afc618-6d04-41e5-bc3c-db140f525ed3" class="bulleted-list"><li style="list-style-type:disc">PATCH /customers/&lt;int:customer_id&gt;</li></ul><ul id="f4eb0eff-5c5b-4b8c-b854-b1660c454fdf" class="bulleted-list"><li style="list-style-type:disc">PATCH /products/&lt;int:product_id&gt;</li></ul><ul id="26a00360-5118-4454-9035-8b719f320052" class="bulleted-list"><li style="list-style-type:disc">PATCH /categories/&lt;int:category_id&gt;</li></ul><ul id="221c14f5-3a7e-4588-8503-53b5b0487c8c" class="bulleted-list"><li style="list-style-type:disc">DELETE /customers/&lt;int:customer_id&gt;</li></ul><ul id="d1d2751a-a0c4-4a73-bcb1-14a705f3e2a3" class="bulleted-list"><li style="list-style-type:disc">DELETE /items/&lt;int:item_id&gt;</li></ul><ul id="1ad4b863-7022-45fa-8e8a-35aed38807f2" class="bulleted-list"><li style="list-style-type:disc">DELETE /products/&lt;int:product_id&gt;</li></ul><ul id="eccea516-aa7e-4c49-9e73-7d7a3ffe51f1" class="bulleted-list"><li style="list-style-type:disc">DELETE /categories/&lt;int:category_id&gt;</li></ul><p id="36979ea0-057d-4b1d-adb5-a4d166197af4" class="">
</p><hr id="ede3709c-8be0-49d8-9f22-4c3edfe1c90e"/><h2 id="e4ed1209-ec50-4d75-a427-4d0564bf8286" class="">Roles and Permission</h2><ul id="8a86fa58-0828-4cfd-86c2-85104dc091fa" class="bulleted-list"><li style="list-style-type:disc">dev - public <ul id="cdfea521-b81e-49d7-91a1-3b1596db5140" class="bulleted-list"><li style="list-style-type:circle">GET /products get all products /</li></ul><ul id="311a837b-e5da-49a2-85c5-014b7eb29564" class="bulleted-list"><li style="list-style-type:circle"> GET /products/&lt;int:product_id&gt; </li></ul><ul id="6de23517-d10d-406f-b125-9253100aa9e9" class="bulleted-list"><li style="list-style-type:circle"> GET /customers/&lt;int:customer_id      </li></ul><ul id="4a3afb8f-415e-4330-82d4-b5c4e0bd03cf" class="bulleted-list"><li style="list-style-type:circle">GET  /customers/int:customer_id/items   gets cart item for a user</li></ul><ul id="4038b1b8-16ca-4e4b-9765-54f568cbcec3" class="bulleted-list"><li style="list-style-type:circle">GET /categories </li></ul><ul id="6a048740-8941-4b02-8e19-fc9cfd75862a" class="bulleted-list"><li style="list-style-type:circle">POST /item</li></ul><ul id="3d272d31-5853-4b7c-a20e-dbfacf56159a" class="bulleted-list"><li style="list-style-type:circle">POST  /customer</li></ul><ul id="9f0ebbaf-126d-4238-a02f-3642fc77a3d3" class="bulleted-list"><li style="list-style-type:circle">PATCH /customers/&lt;int:customer_id&gt;</li></ul><ul id="8190a0f9-656d-4f2e-8ce8-13c687fd434f" class="bulleted-list"><li style="list-style-type:circle">DELETE /customers/&lt;int:customer_id&gt;</li></ul><p id="913d9ce8-cc3c-4d92-ba69-bda4256987b2" class="">
</p></li></ul><ul id="f2de28da-f72d-4ef4-8c2a-f493f88c0084" class="bulleted-list"><li style="list-style-type:disc">product  admin role<ul id="19424dc2-2fe2-4453-961a-17c341a89e30" class="bulleted-list"><li style="list-style-type:circle">all dev - public end points</li></ul><ul id="143d7224-c762-43e4-8a2b-4f74d26df53e" class="bulleted-list"><li style="list-style-type:circle">POST  /product</li></ul><ul id="9e43ba51-dd8f-471b-afb1-fdbb49f07254" class="bulleted-list"><li style="list-style-type:circle">PATCH /products/&lt;int:product_id&gt;</li></ul><ul id="c1c2ee2d-5340-4b93-8c6d-12cf9d59b57e" class="bulleted-list"><li style="list-style-type:circle">DELETE /products/&lt;int:product_id&gt;</li></ul></li></ul><ul id="923555fe-bb79-4bef-a889-b0675f6fb210" class="bulleted-list"><li style="list-style-type:disc">Admin <ul id="a9d94a6e-bc59-4cdf-9cda-2458fb849ee5" class="bulleted-list"><li style="list-style-type:circle">all dev - public end points</li></ul><ul id="3befe3b8-7cf5-4b0c-b34d-12016de0c290" class="bulleted-list"><li style="list-style-type:circle">all product - admin end proints</li></ul><ul id="9aa42d05-7f66-4da6-834f-e6361d7326a8" class="bulleted-list"><li style="list-style-type:circle">POST  /category</li></ul><ul id="7d6c912b-213d-4b9d-b89f-476b314864b6" class="bulleted-list"><li style="list-style-type:circle">PATCH /categories/&lt;int:category_id&gt;</li></ul><ul id="16978037-a63f-4b9f-997b-723a4084c1ab" class="bulleted-list"><li style="list-style-type:circle">DELETE /categories/&lt;int:category_id&gt;</li></ul><p id="c937646a-fa05-4f44-a1cd-e7b5d18550f8" class="">
</p></li></ul><hr id="63ac66ec-5198-4af8-a1b8-73f9a536c117"/><p id="a675d591-02a9-42d8-9b32-f86d29e1a974" class="">
</p><p id="55dec217-93f2-4846-b041-31f90ee345a7" class="">Postman test end points in shopping -api.postman_collection.json file</p><p id="d3bf6e06-7068-4af3-80ec-ac3b0ca4e85f" class="">product role JWT : <div class="indented"><p id="90928793-ffc8-416d-bc7c-e06e7ae2cd1d" style="font-size: 10px;" class="">eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IkNiLV82dmRxTXJ4YUxLV0hKWHRkZyJ9.eyJpc3MiOiJodHRwczovL3VkLWNhcC51cy5hdXRoMC5jb20vIiwic3ViIjoiZ29vZ2xlLW9hdXRoMnwxMTMwMTczNzI2Mzc3ODA3MjMyNjIiLCJhdWQiOiJzaG9waW5nIiwiaWF0IjoxNjM1MDY5NTA3LCJleHAiOjE2MzUwNzY3MDcsImF6cCI6IkJ6enQyOTNRMVh6RW5lVGY2bHQ0RE9OenZWcnJVb1VYIiwic2NvcGUiOiIiLCJwZXJtaXNzaW9ucyI6WyJkZWxldGU6cHJvZHVjdCIsInBhdGNoOnByb2R1Y3QiLCJwb3N0OnByb2R1Y3QiXX0.p0CeBbpp6H7h5K_ax0UkAb0k1NZSh5N_75j_1de1pouO0Td3gpjtpB1sDv08kURQW8z6gqnLWP0n2ADNZuhz5kBT7GmuvgPsFUfM9sy6_ag-_6A84DFQSkAq2dkS_7QEDphgcAJtlRGry7YvU149AVmEzQnG3ijLRjgyW_Rb-k_wtQrTw04hJ4EIrFAuB6Cf-9GoLf2IOLoUnywfrwNM11Qbv8n9Dq6feY9DdXhbQyt4rwhZlVOfRRn7YoqAqgYX8aSPfstMPT9Of_sIlZYeC263LI42YuNqsK9DynSSSkAZRufd24tWMPGX3x105UDXy44PaiKGxw-nuwtsP25vPw </p></div></p><p id="d720d8ba-699a-4ffc-8c9a-2cd2b3d9149d" class="">
</p><p id="73b74d86-b494-419a-a408-cf5f2c7c13b3" class="">Admin JWT :<div class="indented"><p id="a297d7c4-77c0-4be9-90cf-a74761be6081" style="font-size : 10px;" class="">eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IkNiLV82dmRxTXJ4YUxLV0hKWHRkZyJ9.eyJpc3MiOiJodHRwczovL3VkLWNhcC51cy5hdXRoMC5jb20vIiwic3ViIjoiZ29vZ2xlLW9hdXRoMnwxMTEyMzExMDM3Nzk1ODI2OTIzNDYiLCJhdWQiOiJzaG9waW5nIiwiaWF0IjoxNjM1MDY5NzkzLCJleHAiOjE2MzUwNzY5OTMsImF6cCI6IkJ6enQyOTNRMVh6RW5lVGY2bHQ0RE9OenZWcnJVb1VYIiwic2NvcGUiOiIiLCJwZXJtaXNzaW9ucyI6WyJkZWxldGU6Y2F0ZWdvcnkiLCJkZWxldGU6cHJvZHVjdCIsInBhdGNoOmNhdGVnb3J5IiwicGF0Y2g6cHJvZHVjdCIsInBvc3Q6Y2F0ZWdvcnkiLCJwb3N0OnByb2R1Y3QiXX0.Wl7iTDm1ZjNQKy2goBTMTd3ECJrLKRQ7hjsQwPnilExc0CNpgLu1B74zwQ7tWMZyqJ5JCSH2JI8kjaWHiGG7eYWCqcCrVXavpkF2YCGXUFf1iZY6lnK6tnFCx-5vEtOwu7glDvy1KZSxH9p4FZVBx2xqlFXwhVdznbsgO75Ay97ggiws9x67z9MC45T5NMF4CRMGTMxDzkO2EhCkS4ZPPq7TQfTTXPscaK_bdMQJTJ2i7H4Z1MHpWNRzxjSIigyvTC5Q4JOPZuoxZrYhxR-Za7dzydAVcvufO-Q_qZH7ffCLuWddnOrPhWu_EwfcbiUBdZRjL5A2xY02KIsD4u1-eA</p></div></p><p id="98e41e6c-59d8-4ebb-b165-2d77d72483d5" class="">
</p><hr id="82192d89-25c7-4457-b87d-ae6166d66988"/><p id="4add61a5-3b31-4dd4-ae2c-84919d902975" class="">test_end_points.py  File : <div class="indented"><p id="214b7ad0-5274-48ca-b641-5a539a97ff12" class="">unit test for  success and failure  for each end point </p></div></p><p id="416dfa53-5615-40ae-bcd0-5e5d87ec3afa" class="">
</p><hr id="5b781059-adee-44ae-8d8b-9bb8d2dc14a6"/><p id="053b1fb0-7a84-4b9e-b451-e9d547446860" class="">add_data.py File :<div class="indented"><ul id="5682bf9c-99c1-483b-ac20-070b16fc409f" class="bulleted-list"><li style="list-style-type:disc">to be able to run end point unit test </li></ul><ul id="bff79c01-8c5c-4eb8-8b85-1fe8532ae75d" class="bulleted-list"><li style="list-style-type:disc">fill database with data</li></ul></div></p><p id="b7cdebf9-da98-4e7b-99f1-ee90be26ee13" class="">
</p><p id="b7ae3be3-45f7-40c0-b035-06dc29d5a78f" class="">
</p><p id="b332ce66-7351-4127-a1ee-99d60dbf339c" class="">Database design</p><p id="79004483-54cb-4d7e-8687-3cd7f48985eb" class="">
</p><figure id="9f4bd29d-a054-4e1c-8da3-f84d74b98e9a" class="image"><a href="Shopping%20-%20Store%209f4bd29da0544e1c8da3f84d74b98e9a/database.png"><img style="width:838px" src="database-design/database.png"/></a></figure><p id="86d9a6ab-a60c-4b1a-be7f-3ad28f28c4a1" class="">
</p></div></article></body></html>