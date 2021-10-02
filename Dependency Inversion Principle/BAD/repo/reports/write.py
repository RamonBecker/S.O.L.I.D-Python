from .file_write import ReportFileWriter


class ReportWrite():
    @staticmethod
    def write(report):
        ReportFileWriter.write_file(report)
