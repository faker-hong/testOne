#-*- coding:utf-8 -*-
import sys, os, subprocess
from http.server import BaseHTTPRequestHandler,HTTPServer
#-------------------------------------------------------------------------------

class ServerException(Exception):
    '''�������ڲ�����'''
    pass

#-------------------------------------------------------------------------------

class base_case(object):
    '''�����������'''

    def handle_file(self, handler, full_path):
        try:
            with open(full_path, 'rb') as reader:
                content = reader.read()
            handler.send_content(content)
        except IOError as msg:
            msg = "'{0}' cannot be read: {1}".format(full_path, msg)
            handler.handle_error(msg)

    def index_path(self, handler):
        return os.path.join(handler.full_path, 'index.html')

    def test(self, handler):
        assert False, 'Not implemented.'

    def act(self, handler):
        assert False, 'Not implemented.'

#-------------------------------------------------------------------------------

class case_no_file(base_case):
    '''�ļ���Ŀ¼������'''

    def test(self, handler):
        return not os.path.exists(handler.full_path)

    def act(self, handler):
        raise ServerException("'{0}' not found".format(handler.path))

#-------------------------------------------------------------------------------

class case_cgi_file(base_case):
    '''��ִ�нű�'''

    def run_cgi(self, handler):
        data = subprocess.check_output(["python3", handler.full_path],shell=False)
        handler.send_content(data)

    def test(self, handler):
        return os.path.isfile(handler.full_path) and \
               handler.full_path.endswith('.py')

    def act(self, handler):
        self.run_cgi(handler)

#-------------------------------------------------------------------------------

class case_existing_file(base_case):
    '''�ļ����ڵ����'''

    def test(self, handler):
        return os.path.isfile(handler.full_path)

    def act(self, handler):
        self.handle_file(handler, handler.full_path)

#-------------------------------------------------------------------------------

class case_directory_index_file(base_case):
    '''�ڸ�·���·�����ҳ�ļ�'''

    def test(self, handler):
        return os.path.isdir(handler.full_path) and \
               os.path.isfile(self.index_path(handler))

    def act(self, handler):
        self.handle_file(handler, self.index_path(handler))

#-------------------------------------------------------------------------------

class case_always_fail(base_case):
    '''Ĭ�ϴ���'''

    def test(self, handler):
        return True

    def act(self, handler):
        raise ServerException("Unknown object '{0}'".format(handler.path))

#-------------------------------------------------------------------------------

class RequestHandler(BaseHTTPRequestHandler):
    '''
    ����·���Ϸ��򷵻���Ӧ����
    ���򷵻ش���ҳ��
    '''

    Cases = [case_no_file(),
             case_cgi_file(),
             case_existing_file(),
             case_directory_index_file(),
             case_always_fail()]

    # ����ҳ��ģ��
    Error_Page = """\
        <html>
        <body>
        <h1>Error accessing {path}</h1>
        <p>{msg}</p>
        </body>
        </html>
        """

    def do_GET(self):
        try:

            # �õ�����������·��
            self.full_path = os.getcwd() + self.path
            # �������е����������
            for case in self.Cases:
                if case.test(self):
                    case.act(self)
                    break

        # �����쳣
        except Exception as msg:
            self.handle_error(msg)

    def handle_error(self, msg):
        content = self.Error_Page.format(path=self.path, msg=msg)
        self.send_content(content.encode("utf-8"), 404)

    # �������ݵ��ͻ���
    def send_content(self, content, status=200):
        self.send_response(status)
        self.send_header("Content-type", "text/html")
        self.send_header("Content-Length", str(len(content)))
        self.end_headers()
        self.wfile.write(content)

#-------------------------------------------------------------------------------

if __name__ == '__main__':
    serverAddress = ('', 8080)
    server = HTTPServer(serverAddress, RequestHandler)
    server.serve_forever()
