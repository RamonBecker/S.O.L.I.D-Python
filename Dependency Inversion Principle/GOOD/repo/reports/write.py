from .file_write import ReportFileWriter


class ReportWrite():
    @staticmethod
    def write(report, writer=ReportFileWriter):
        writer.write(report)
