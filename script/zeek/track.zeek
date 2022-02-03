@load base/frameworks/logging

@load base/protocols/conn
@load base/protocols/http

@load ./post_body.zeek

module track;

event zeek_init() {
    print "hello";
}
global request = 0;
redef record HTTP::Info += {
	subrequest: int &log &optional;
};

event http_request(c: connection, method: string, original_uri: string, unescaped_uri: string, version: string) {
    if(c$id$resp_p == 8060/tcp) {
        request = request + 1;
        c$http$subrequest = request;
    }
    else {
        c$http$subrequest = request;
    }
}

event zeek_done() {
    print "goodbye";
}