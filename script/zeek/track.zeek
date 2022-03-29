@load base/frameworks/logging

@load base/protocols/conn
@load base/protocols/http

@load ./post_body.zeek

module track;
export {
    option bff_port = 3000/tcp;
}
event zeek_init() {
    print fmt("tracking port as bff: %d", bff_port);
}
global request = 0;
redef record HTTP::Info += {
	subrequest: int &log &optional;
};
 
event http_request(c: connection, method: string, original_uri: string, unescaped_uri: string, version: string) {
    if(c$id$resp_p == bff_port) {
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