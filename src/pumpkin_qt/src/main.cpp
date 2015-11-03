/**
 * @file /src/main.cpp
 *
 * @brief Qt based gui.
 *
 * @date November 2010
 **/
/*****************************************************************************
** Includes
*****************************************************************************/

#include <QtGui>
#include <QApplication>

#include "pumpkinqt.hpp"

/*****************************************************************************
** Main
*****************************************************************************/

int main(int argc, char **argv) {

    /*********************
    ** Qt
    **********************/
    QApplication app(argc, argv);

	QFont mainFont("Ubuntu", 16);
	app.setFont(mainFont);

    //pumpkin_qt::MainWindow w(argc,argv);
    pumpkin_qt::PumpkinQT w(argc, argv);
	w.setWindowState(w.windowState() | Qt::WindowMaximized);
    w.show();
    app.connect(&app, SIGNAL(lastWindowClosed()), &app, SLOT(quit()));
    int result = app.exec();

	return result;
}
